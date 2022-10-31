from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.solar_system import Planet

# class Planet:
#     def __init__(self, id, name, descripiton, radius):
#         self.id = id
#         self.name = name
#         self.description = descripiton
#         self.radius = radius

# planet_list = [
#     Planet(1, "Mars", "Red planet",  2106.1),
#     Planet(2, "Saturn", "Planet with rings", 36184),
#     Planet(3, "Neptune", "Farthest planet", 15299),
#     Planet(4, "Mercury", "Closest to the sun", 1516)
# ]

planet_bp = Blueprint("planet_bp",__name__, url_prefix="/planet")

# @planet_bp.route('', methods=['GET'])
# def get_all_planets():
#     result = []
#     for planet in planet_list:
#         planet_dict = {"id":planet.id, "name":planet.name,
#                         "description":planet.description, "radius":planet.radius}
#         result.append(planet_dict)
#     return jsonify(result), 200

@planet_bp.route('/<planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"msg": f"Invalid data type {planet_id}"}), 400
    
    chosen_planet = Planet.query.get(planet_id)

    # for planet in planet_list:
    #     if planet.id==planet_id:
    #         chosen_planet = planet
    
    if chosen_planet is None:
        return jsonify({"msg": f"Could not find a planet with id: {planet_id}"}), 404

    return_planet = {
        "id": chosen_planet.id, 
        "name": chosen_planet.name, 
        "description": chosen_planet.description,
        "radius": chosen_planet.radius
    }
    return jsonify(return_planet), 200
        
@planet_bp.route('', methods=["POST"])
def create_one_planet():
    request_body = request.get_json()

    new_planet = Planet( 
                        name=request_body['name'],
                        description=request_body['description'],
                        radius=request_body['radius']
                        )
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({'msg':f'Successfully created Planet with id = {new_planet.id}'}), 201

@planet_bp.route('',methods=['GET'])
def get_all_planets():
    result = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        planet_dict = {"id":planet.id, "name":planet.name,
                        "description":planet.description, "radius":planet.radius}
        result.append(planet_dict)
    return jsonify(result), 200