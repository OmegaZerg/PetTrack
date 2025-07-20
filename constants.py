from enum import Enum

TEST_FILE = "pets_test.json"
PROD_FILE = "pets.json"

class MenuHeader(Enum):
    MAIN_1 = "| Hello from Pet-Track! |"
    MAIN_2 = "| Main Menu |"
    PROF_MGMNT = "| Pet Profile Management |"
    CREATE_1 = "| Create Pet Profile |"
    CREATE_2 = "/Ex: Lucky Dog 4 M Black\\"

class UserInput(Enum):
    MAIN_MENU = "Please select from one of the following options:\n1. View/Manage pet profiles\n2. View/Manage mealtime data\n3. View/Manage reminders\n4. View blog\n9. Exit Pet_track\n"
    MANAGE_PETS = "Please select from one of the following options:\n1. View an existing pet profile\n2. Edit an existing pet profile\n3. Create a new pet profile\n9. Return to the main menu\n"
    CREATE_PROFILE = "To create a new pet profile, enter 5 values separated by spaces in the following order. (Also reference the above template under this menu's header): Animal_Name | Type | Age | Gender | Color\n"
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

GENDERS = {
    1: "┌───────────────────┐",
    2: "|   Valid Genders:  |",
    3: "| 1. M              |",
    4: "| 2. F              |",
    5: "└───────────────────┘"
}

TYPES = {
    1: "┌───────────────────────────────┐",
    2: "|         Valid Types:          |",
    3: "| 1. Dog          8. Fish       |",
    4: "| 2. Cat          9. Snake      |",
    5: "| 3. Bird         10. Turtle    |",
    6: "| 4. Rabbit       11. Iguana    |",
    7: "| 5. Hamster      12. Lizard    |",
    8: "| 6. Ferret       13. Other     |",
    9: "| 7. Guinea Pig                 |",
    10: "└───────────────────────────────┘"
}

COLORS = {
    1: "┌───────────────────────────────┐",
    2: "|         Valid Colors:         |",
    3: "| 1. Black        8. Other      |",
    4: "| 2. Blue         9. Pink       |",
    5: "| 3. Brown        10. Red       |",
    6: "| 4. Green        11. White     |",
    7: "| 5. Orange       12. Yellow    |",
    8: "└───────────────────────────────┘"
}