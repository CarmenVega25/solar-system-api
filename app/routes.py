from flask import abort, Blueprint, jsonify, make_response, request
from app import db
from app.models.solar_system import Planet

# planet_list = [
#     Planet(1, "Mars", "Red planet",  2106.1),
#     Planet(2, "Saturn", "Planet with rings", 36184),
#     Planet(3, "Neptune", "Farthest planet", 15299),
#     Planet(4, "Mercury", "Closest to the sun", 1516)
# ]

planet_bp = Blueprint("planet_bp",__name__, url_prefix="/planet")

@planet_bp.route('/<planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    chosen_planet = get_model_from_id(Planet, planet_id)
    return jsonify(chosen_planet.to_dict()), 200
        
@planet_bp.route('', methods=["POST"])
def create_one_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)

    # new_planet = Planet( 
    #                     name=request_body['name'],
    #                     description=request_body['description'],
    #                     radius=request_body['radius']
    #                     )
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({'msg':f'Successfully created Planet with id = {new_planet.id}'}), 201

@planet_bp.route('',methods=['GET'])
def get_all_planets():
    name_query_value = request.args.get('name')
    
    if name_query_value is not None:
        planets = Planet.query.filter_by(name=name_query_value)
    else:
        planets = Planet.query.all()
    
    result = []
    for planet in planets:
        result.append(planet.to_dict())
    return jsonify(result), 200

@planet_bp.route('/<planet_id>', methods=['PUT'])
def update_one_planet_id(planet_id):
    update_planet = get_model_from_id(Planet, planet_id)
    request_body = request.get_json()

    try:
        update_planet.name = request_body["name"]
        update_planet.description = request_body["description"]
        update_planet.radius = request_body["radius"]
    except KeyError:
        return jsonify({"msg": f"Missing needed data"}), 400
    
    db.session.commit()
    return jsonify({"msg": f"Successfulyl updated planet with id {update_planet.id}"}), 200

def get_model_from_id(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        return abort(make_response({"msg": f"Invalid data type {model_id}"}, 400))
    
    chosen_object = cls.query.get(model_id)

    if chosen_object is None:
        return abort(make_response({"msg": f"Could not find a {cls.__name__} with id: {model_id}"}, 404))
    
    return chosen_object

@planet_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    planet_to_delete = get_model_from_id(Planet, planet_id)
    db.session.delete(planet_to_delete)
    db.session.commit()
    return jsonify({"msg":f"Successfully deleted planet with id {planet_to_delete.id}"}), 200