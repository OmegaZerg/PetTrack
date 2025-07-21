import json
import os
from constants import *
from classes import *
from random import randint

def display_pet_profile_by_id(pet_id: str, config: str = None):
    if not pet_id.startswith("PT_"):
        print("Pet ID is required to start with 'PT_'. Please enter a valid ID.")
        return
    
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
        
        if config == "short":
            print(f"Pet ID: {pet_id} -> Name: {pets[pet_id]["name"]}, Type: {pets[pet_id]["type"]}, Age: {pets[pet_id]["age"]}, Gender: {pets[pet_id]["gender"]}, Color: {pets[pet_id]["color"]}")
        else:
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

def get_pet_profile_by_id(pet_id: str) -> PetProfile:
    if not pet_id.startswith("PT_"):
        print("Pet ID is required to start with 'PT_'. Please enter a valid ID.")
        return
    if not os.path.exists(TEST_FILE):
        print("ERROR: Unable to find the pets.json file in this directory. Please create a pet profile first!")
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
            pet_count = int(pets["total_entries"])
    except Exception as e:
        print(f"ERROR: {e}")
    
    #Temp counting here until implemented in function validate_pet_profile
    print(f"total entries: {pet_count}")
    dic_length = len(pets)
    print(f"pets length: {dic_length-1}")

    return PetProfile(pets[pet_id]["name"], pets[pet_id]["type"], pets[pet_id]["age"], pets[pet_id]["gender"], pets[pet_id]["color"])

def search_pets(pet_id: str = "", name: str = "", type: str = ""):
    pass

def menu_display_pet_profiles(num: int):
    #Get up to num pet profiles to display
    if not os.path.exists(TEST_FILE):
        sample_1 = PetProfile("Lucky", "Dog", 4, "M", "Brown")
        sample_2 = PetProfile("Lucy", "Cat", 8, "F", "Black")
        print("Add pets by visiting the 'Create Pet Profile' menu. Showing samples:")
        print(sample_1)
        print(sample_2)
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
            pet_count = int(pets["total_entries"])
    except Exception as e:
        print(f"ERROR: {e}")

    if pet_count >= num:
        #TODO: Add logic so that if a pet profile has already been selected for display, it will not be selected again. <-------------------
        for i in range(num):
            profile_id = randint(1, pet_count)
            display_pet_profile_by_id(f"PT_{profile_id}", "short")
    else:
        profile_id = 1
        for pet in pets:
            display_pet_profile_by_id(f"PT_{profile_id}", "short")
            profile_id += 1
    #TODO Need to run more testing on this function <-------------------


def validate_pet_entries():
    #Check json data, loop through each entry and compare to the 'total_entries'. If they are not the same, update total entries then log out to a file that a discrepancy was found and corrected.
    pass

def create_pet_profile(pet: PetProfile):
    #Replace test file with prod file later
    #TODO: Add special logic to look for and handle gaps in pet IDs. So after deletetion, we can have gaps if the delete was done anywhere but the last entry. Possibly add a new data member to the json file to store these gaps, then check that first for a free ID to assign back out. <-------------------

    if not os.path.exists(TEST_FILE):
        empty_pets = {"total_entries": 0}
        with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
            json.dump(empty_pets, write_file)
    
    new_pet = {
        "name": pet.name,
        "type": pet.type,
        "age": pet.age,
        "gender": pet.gender,
        "color": pet.color
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
            valid_input = ["1", "2", "3", "4", "9"]
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
                    valid_input.append(False)
                    continue
                except Exception as e:
                    print(f"Unknown Error: {e}")
                    valid_input.append(False)
                    continue
                if not name:
                    valid_input.append(False)
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
            #     print(f"Valid Input(Inside loop): {valid_input}")
            # print(f"Valid Input: {valid_input}") 
            return PetProfile(name, type, age, gender, color)
        case UserInput.DELETE_PROFILE:
            valid_input = ["y", "yes", "n", "no"]
            choice = input(text.value).lower()
            while choice not in valid_input:
                choice = input(text.value)
            return choice
        case _:
            print("ERROR: Somehow we made it to the get_user_input function without a valid user input ENUM!")

def display_valid_pet_inputs():
    for line in GENDERS:
        print(GENDERS[line])
    for line in TYPES:
        print(TYPES[line])
    for line in COLORS:
        print(COLORS[line])