class PetProfile():
    def __init__(self, name: str, type: str, age: int, gender: str, color: str):
        self.name = name
        self.type = type
        self.age = age
        self.gender = gender
        self.color = color

    def __repr__(self):
        return f"Pet Profile -> Name: {self.name}, Type: {self.type}, Age: {self.age}, Gender: {self.gender}, Color: {self.color}"