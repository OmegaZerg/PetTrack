from enum import Enum

TEST_FILE = "pets_test.json"
PROD_FILE = "pets.json"

class UserInput(Enum):
    MAIN_MENU = "Please select from one of the following options:\n1. View/Manage pet profiles\n2. View/Manage mealtime data\n3. View/Manage reminders\n4. View blog\n9. Exit Pet_track\n"
    MANAGE_PETS_MENU = "Please select from one of the following options:\n1. View an existing pet profile\n2. Edit an existing pet profile\n3. Create a new pet profile\n9. Return to the main menu\n"
    DELETE_PROFILE = "Are you sure you wish to delete the above pet profile?\nType 'Y or Yes' to confirm deletetion, type 'N or No' to abort deletion and keep this pet profile.\n"

class PetColor(Enum):
    BLACK = "Black"
    BROWN = "Brown"
    WHITE = "White"
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    PINK = "Pink"
    OTHER = "Other"

class PetGender(Enum):
    MALE = "M"
    FEMALE = "F"

class PetType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    BIRD = "Bird"
    RABBIT = "Rabbit"
    HAMSTER = "Hamster"
    FERRET = "Ferret"
    GUINEA = "Guinea Pig"
    FISH = "Fish"
    SNAKE = "Snake"
    TURTLE = "Turtle"
    IGUANA = "Iguana"
    LIZARD = "Lizard"
    OTHER = "Other"