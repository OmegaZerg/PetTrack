import json
import os
from constants import *

def display_pet_profile_by_id(pet_id: str):
    if not pet_id.startswith("PT_"):
        print("Pet ID is required to start with 'PT_'. Please enter a valid ID.")
        return
    
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
            print(f"-----| Displaying pet profile for ID: {pet_id} |-----\n")
            print(f"{pets[pet_id]}")
    except KeyError as ke:
        print(f"ERROR: Unable to find pet ID: {ke}!")
    except Exception as e:
        print(f"ERROR: {e}")

def search_pets(pet_id: str = "", name: str = "", type: str = ""):
    pass

def menu_get_pet_profiles(void):
    #Get up to 5 pet profiles to display
    pass

def create_pet_profile(name: str, type: str, age: int, gender: str, color: str):
    #Replace test file with prod file later
    #TODO: Add special logic to look for and handle gaps in pet IDs. So after deletetion, we can have gaps if the delete was done anywhere but the last entry. Possibly add a new data member to the json file to store these gaps, then check that first for a free ID to assign back out.

    if not os.path.exists(TEST_FILE):
        empty_pets = {"total_entries": 0}
        with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
            json.dump(empty_pets, write_file)
    
    new_pet = {
        "name": name,
        "type": type,
        "age": age,
        "gender": gender,
        "color": color
    }

    with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
        pets = json.load(read_file)
        pet_count = int(pets["total_entries"])

    new_pet_count = pet_count + 1
    new_pet_id = f"PT_{new_pet_count}"

    with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
        pets["total_entries"] = new_pet_count
        pets[new_pet_id] = new_pet
        json.dump(pets, write_file, indent=4)

def delete_pet_profile_by_id(pet_id: str):
    if not os.path.exists(TEST_FILE):
        raise Exception(f"ERROR: File path to pets data does not exist. Unable to delete Pet ID: {pet_id}")
    with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
        pets = json.load(read_file)

    if pet_id in pets:
        print("Pet Found!")
        pet_to_remove = pets[pet_id]
        #TODO: Need function to display "cleaned" pet profile
        display_pet_profile_by_id(pet_id)
        confirm_delete = get_user_input(UserInput.DELETE_PROFILE).lower()
        if confirm_delete == "y" or confirm_delete == "yes":
            pets.pop(pet_id)
            pets["total_entries"] -= 1
            with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(pets, write_file, indent=4)
            print("Pet profile successfully deleted")
        elif confirm_delete == "n" or confirm_delete == "no":
            pets[pet_id] = pet_to_remove
            with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(pets, write_file, indent=4)
            print(f"Pet with ID: {pet_id} was not deleted.")

    else:
        print(f"Unable to find Pet ID: {pet_id}. Delete operation canceled!")


def get_user_input(text: UserInput) -> int | str:
    match text:
        case UserInput.MAIN_MENU:
            valid_input = [1, 2, 3]
            choice = int(input(text.value))
            while choice not in valid_input:
                choice = int(input(text.value))
            return choice
        case UserInput.DELETE_PROFILE:
            valid_input = ["y", "yes", "n", "no"]
            choice = input(text.value)
            while choice not in valid_input:
                choice = input(text.value)
            return choice
    