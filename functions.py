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

        #possible setting to add for config later, for now commenting out profile1
        #pretty print profile1
        # id = f"[ Pet Profile ID: {pet_id} ]"
        # name = f"[ Pet Name: {pets[pet_id]["name"]} ]"
        # type = f"[ Pet Type: {pets[pet_id]["type"]} ]"
        # age = f"[ Pet Age: {pets[pet_id]["age"]} ]"
        # gender = f"[ Pet Gender: {pets[pet_id]["gender"]} ]"
        # color = f"[ Pet Color: {pets[pet_id]["color"]} ]"
        # print(f"{id:{'-'}^50}")
        # print(f"{name:{'-'}^50}")
        # print(f"{type:{'-'}^50}")
        # print(f"{age:{'-'}^50}")
        # print(f"{gender:{'-'}^50}")
        # print(f"{color:{'-'}^50}")

        #pretty print profile2
        print()
        id = f"[ Pet Profile ID: {pet_id} ]"
        name = f"[ Pet Name      : {pets[pet_id]["name"]} ]"
        type = f"[ Pet Type      : {pets[pet_id]["type"]} ]"
        age = f"[ Pet Age       : {pets[pet_id]["age"]} ]"
        gender = f"[ Pet Gender    : {pets[pet_id]["gender"]} ]"
        color = f"[ Pet Color     : {pets[pet_id]["color"]} ]"
        print(f"{id:{'-'}<50}")
        print(f"{name:{'-'}<50}")
        print(f"{type:{'-'}<50}")
        print(f"{age:{'-'}<50}")
        print(f"{gender:{'-'}<50}")
        print(f"{color:{'-'}<50}")

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

    display_pet_profile_by_id(new_pet_id)

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
        confirm_delete = get_user_input(UserInput.DELETE_PROFILE)
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
            valid_input = ["1", "2", "3", "4", "9"]
            choice = input(text.value)
            while choice not in valid_input:
                choice = input(text.value)
            return int(choice)
        case UserInput.MANAGE_PETS:
            valid_input = ["1", "2", "3", "9"]
            choice = input(text.value)
            while choice not in valid_input:
                choice = input(text.value)
            return int(choice)
        case UserInput.CREATE_PROFILE:
            valid_input = [False]
            while not all(valid_input):
                valid_input = []
                try:
                    name, type, age, gender, color = input(text.value).split()
                except ValueError as ve:
                    print(f"Invalid Input Received: {ve}")
                    continue
                except Exception as e:
                    print(f"Unknown Error: {e}")
                    continue
                if type in [item.value for item in PetType]:
                    valid_input.append(True)
                else:
                    print("Invalid type")
                    valid_input.append(False)
                if age.isnumeric():
                    age = int(age)
                    valid_input.append(True)
                else:
                    print("Non-Numeric Age")
                    valid_input.append(False)
                if gender in [item.value for item in PetGender]:
                    valid_input.append(True)
                else:
                    print("Invalid gender")
                    valid_input.append(False)
                if color in [item.value for item in PetColor]:
                    valid_input.append(True)
                else:
                    print("Invalid color")
                    valid_input.append(False)
                print(f"Valid Input: {valid_input}")
            print(f"Valid Input: {valid_input}")
            return name, type, age, gender, color
                

        case UserInput.DELETE_PROFILE:
            valid_input = ["y", "yes", "n", "no"]
            choice = input(text.value).lower()
            while choice not in valid_input:
                choice = input(text.value)
            return choice
        case _:
            print("ERROR: Somehow we made it to the get_user_input function without a valid user input ENUM!")