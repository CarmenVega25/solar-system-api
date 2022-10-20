from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, descrpiton, radius):
        self.id = id
        self.name = name
        self.description = descrpiton
        self.radius = radius

planet_list = [
    Planet(1, "Mars", "Red planet",  2,106.1),
    Planet(2, "Saturn", "Planet with rings", 36,184),
    Planet(3, "Neptune", "Farthest planet", 15,299),
    Planet(4, "Mercury", "Closest to the sun", 1,516)
    ]

planet_bp = Blueprint("planets",__name__, url_prefix="/planets")

@planet_bp.route('', methods=['GET'])
def get_all_planets():
    result = []
    for planet in planet_list:
        planet_dict = {"id":planet.id, "name":planet.name,
                        "description":planet.description, "radius":planet.radius}
        result.append(planet_dict)
    return jsonify(result), 200