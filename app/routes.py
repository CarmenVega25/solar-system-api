from flask import Blueprint

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