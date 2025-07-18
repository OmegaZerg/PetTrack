from enum import Enum

TEST_FILE = "pets_test.json"
PROD_FILE = "pets.json"

class UserInput(Enum):
    MAIN_MENU = "Please select from one of the following options:\n1. Edit an existing profile\n2. Create a new profile\n3. View blog\n"
    DELETE_PROFILE = "Are you sure you wish to delete the above pet profile?\nType 'Y or Yes' to confirm deletetion, type 'N or No' to abort deletion and keep this pet profile.\n"