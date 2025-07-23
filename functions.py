import json
import os
from constants import *
from classes import *
from random import randint
import logging
logger = logging.getLogger(__name__)

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
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "display_pet_profile_by_id")

def get_pet_profile_by_id(pet_id: str) -> PetProfile:
    if not pet_id.startswith("PT_"):
        print("Pet ID is required to start with 'PT_'. Please enter a valid ID.")
        return
    if not os.path.exists(TEST_FILE):
        generate_log(LogLevel.WARNING, f"Unable to find the pets.json file in directoryL {TEST_FILE}. Please create a pet profile first!")
        print("ERROR: Unable to find the pets.json file in this directory. Please create a pet profile first!")
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "get_pet_profile_by_id")
        return
    
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
        sample_1 = PetProfile("Lucky", "Dog", 4, "M", "Brown")
        print(f"Pet ID: Sample -> {sample_1}")
        generate_log(LogLevel.ERROR, f"Issue with displaying auto generated pet: {e}", "menu_display_pet_profiles")

    if pet_count >= num:
        #TODO: Add logic so that if a pet profile has already been selected for display, it will not be selected again. <-------------------
        #TODO: Needs to be smarter to where it only picks from an actual valid list. SO right now its just picking based on 1 through the pet count. but if there are empty slots (pets deleted) then this will potentially cause an error to display for 'unable to find pet id'. fix 2 birds 1 stone; change to random choice, populate choice list based on range of 1, pet_count but remove the empty slots. <-------------------
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
    if not os.path.exists(TEST_FILE):
        generate_log(LogLevel.CRITICAL, "Unable to find JSON pet data file during validation of pet entries.", "validate_pet_entries")
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
    except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "validate_pet_entries")
    
    pet_count = int(pets["total_entries"])
    num_pets = len(pets) -1
    if pet_count != num_pets:
        generate_log(LogLevel.WARNING, f"Entry count and pet profile count mis-match. Total entries was: {pet_count}, while number of pets is: {num_pets}!", "validate_pet_entries")
        pets["total_entries"] = num_pets
        try:
            with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(pets, write_file, indent=4)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "validate_pet_entries")
            return
        #TODO: Fix the issue <-------------------
    else:
        generate_log(LogLevel.INFO, "pets.json file integrity validated, no correction required.", "validate_pet_entries")
    #TODO: Sweep process: check for empty slots and append to list in json file. Check that empty_slots exists, if not then add to json file. Append any empty slots to the list if they arent already in there. <-------------------
    #TODO: Once that is in place, need to add a check for empty slots into create_pet_profile to use empty slots before generating a new ID. <-------------------


def create_pet_profile(pet: PetProfile):
    #Replace test file with prod file later
    #TODO: Add special logic to look for and handle gaps in pet IDs. So after deletetion, we can have gaps if the delete was done anywhere but the last entry. Possibly add a new data member to the json file to store these gaps, then check that first for a free ID to assign back out. <-------------------

    if not os.path.exists(TEST_FILE):
        empty_pets = {"total_entries": 0, "empty_slots": []}
        try:
            with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(empty_pets, write_file)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "create_pet_profile")
    
    new_pet = {
        "name": pet.name,
        "type": pet.type,
        "age": pet.age,
        "gender": pet.gender,
        "color": pet.color
    }
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
            pet_count = int(pets["total_entries"])
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "create_pet_profile")

    new_pet_count = pet_count + 1
    new_pet_id = f"PT_{new_pet_count}"

    try:
        with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
            pets["total_entries"] = new_pet_count
            pets[new_pet_id] = new_pet
            json.dump(pets, write_file, indent=4)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "create_pet_profile")

    display_pet_profile_by_id(new_pet_id)

def delete_pet_profile_by_id(pet_id: str):
    if not os.path.exists(TEST_FILE):
        generate_log(LogLevel.ERROR, f"File path to pets data does not exist. Unable to delete Pet ID: {pet_id}", "delete_pet_profile_by_id")
        raise Exception(f"ERROR: File path to pets data does not exist. Unable to delete Pet ID: {pet_id}")
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "delete_pet_profile_by_id")

    if pet_id in pets:
        print("Pet Found!")
        pet_to_remove = pets[pet_id]
        display_pet_profile_by_id(pet_id)
        confirm_delete = get_user_input(UserInput.DELETE_PROFILE)
        if confirm_delete == "y" or confirm_delete == "yes":
            pets.pop(pet_id)
            pets["total_entries"] -= 1
            try:
                with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                    json.dump(pets, write_file, indent=4)
            except Exception as e:
                generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "delete_pet_profile_by_id")
            print("Pet profile successfully deleted")
            input("Press Enter to continue...")
        elif confirm_delete == "n" or confirm_delete == "no":
            pets[pet_id] = pet_to_remove
            try:
                with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                    json.dump(pets, write_file, indent=4)
            except Exception as e:
                generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "delete_pet_profile_by_id")
            print(f"Pet with ID: {pet_id} was not deleted.")
            input("Press Enter to continue...")
        #TODO: Added to end of function, need to test that this works <-------------------
        validate_pet_entries()

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
            generate_log(LogLevel.ERROR, "Function called without a valid UserInput enum", "get_user_input")

def display_valid_pet_inputs():
    for line in GENDERS:
        print(GENDERS[line])
    for line in TYPES:
        print(TYPES[line])
    for line in COLORS:
        print(COLORS[line])

def generate_log(level: LogLevel, log_message: str, func_name: str):
    #TODO: Have tempoarily have added a truncate_limit constant to be used. This will need to be changed to use a settings.json file instead in the future. <-------------------
    if not os.path.exists("logs/"):
        os.mkdir("logs/")
        
    logging.basicConfig(level=logging.INFO, filename=LOG_FILE, filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

    match level.value:
        case 0:
            logger.info(f"{log_message} - {func_name}")
        case 1:
            logger.warning(f"{log_message} - {func_name}")
        case 2:
            logger.error(f"{log_message} - {func_name}")
        case 3:
            logger.critical(f"{log_message} - {func_name}")
        case _:
            print("Invalid logger level")
            input("Press Enter to continue...")
    
    try:
        with open(LOG_FILE, mode="r", encoding="utf-8") as read_file:
            line_count = sum(1 for _ in read_file)
    except Exception as e:
        print(f"ERROR: Unable to open the log file. {e}")
        return
    
    if line_count > TRUNCATE_LIMIT:
        try:
            with open(LOG_FILE, mode="r", encoding="utf-8") as file:
                lines = file.readlines()
                file.close()
        except Exception as e:
            print(f"ERROR: Unable to open the log file. {e}")
        try:
            truncated_file = [line for i, line in enumerate(lines) if i > line_count - TRUNCATE_LIMIT]
            with open(LOG_FILE, mode="w", encoding="utf-8") as file:
                file.writelines(truncated_file)
                file.close()
        except Exception as e:
            print(f"ERROR: Unable to truncate the log file. {e}")
