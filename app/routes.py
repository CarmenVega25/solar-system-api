from flask import Blueprint

class Planet:
    def __init__(self, id, name, descrpiton, mass):
        self.id = id
        self.name = name
        self.description = descrpiton
        self.mass = mass