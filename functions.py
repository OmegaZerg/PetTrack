import json
def get_pet_profile_by_id(pet_id: str):
    with open("pets.json", mode="r", encoding="utf-8") as read_file:
        pets = json.load(read_file)
        print(f"-----| Displaying pet profile for ID: {pet_id} |-----\n")
        print(f"{pets[pet_id]}")

def search_pets(pet_id: str = "", name: str = "", type: str = ""):
    pass

def menu_get_pet_profiles(void):
    pass

def create_pet_profile():
    pass

def get_user_input(text: str) -> int:
    valid_input = [1, 2, 3]
    choice = int(input(text))

    while choice not in valid_input:
        choice = int(input(text))

    return choice