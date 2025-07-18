import json
import os

def get_pet_profile_by_id(pet_id: str):
    if not pet_id.startswith("PT_"):
        print("Pet ID is required to start with 'PT_'. Please enter a valid ID.")
        return
    
    with open("pets.json", mode="r", encoding="utf-8") as read_file:
        pets = json.load(read_file)
        print(f"-----| Displaying pet profile for ID: {pet_id} |-----\n")
        print(f"{pets[pet_id]}")

def search_pets(pet_id: str = "", name: str = "", type: str = ""):
    pass

def menu_get_pet_profiles(void):
    #Get up to 5 pet profiles to display
    pass

def create_pet_profile(name: str, type: str, age: int, gender: str, color: str):
    #Replace test file with real file later
    test_file = "pets_test.json"
    prod_file = "pets.json"

    if not os.path.exists(test_file):
        empty_pets = {"total_entries": 0}
        with open(test_file, mode="w", encoding="utf-8") as write_file:
            json.dump(empty_pets, write_file)
    
    new_pet = {
        "name": name,
        "type": type,
        "age": age,
        "gender": gender,
        "color": color
    }

    with open(test_file, mode="r", encoding="utf-8") as read_file:
        pets = json.load(read_file)
        pet_count = int(pets["total_entries"])

    new_pet_count = pet_count + 1
    new_pet_id = f"PT_{new_pet_count}"

    with open(test_file, mode="w", encoding="utf-8") as write_file:
        pets["total_entries"] = new_pet_count
        pets[new_pet_id] = new_pet
        print(f"new dic: {pets}")
        json.dump(pets, write_file, indent=4)


def get_user_input(text: str) -> int:
    valid_input = [1, 2, 3]
    choice = int(input(text))

    while choice not in valid_input:
        choice = int(input(text))

    return choice