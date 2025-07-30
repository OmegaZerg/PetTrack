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
        
        if pet_id not in pets:
            print(f"Unable to find pet ID: {pet_id}! Try again!")
            return

        if config == "short":
            print(f"Pet ID: {pet_id} -> Name: {pets[pet_id]["name"]}, Type: {pets[pet_id]["type"]}, Age: {pets[pet_id]["age"]}, Gender: {pets[pet_id]["gender"]}, Color: {pets[pet_id]["color"]}")
        else:
            print(f"\n-----| Displaying pet profile for ID: {pet_id} |-----\n")
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
        generate_log(LogLevel.WARNING, f"Unable to find the pets.json file in directory  {TEST_FILE}. Please create a pet profile first!")
        print("ERROR: Unable to find the pets.json file in this directory. Please create a pet profile first!")
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
        if pet_id not in pets:
            print(f"Unable to find pet ID: {pet_id}! Try again!")
            return
    except KeyError as ke:
        print(f"ERROR: Unable to find pet ID: {ke}!")
        return
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "get_pet_profile_by_id")
        return
    
    return PetProfile(pets[pet_id]["name"], pets[pet_id]["type"], pets[pet_id]["age"], pets[pet_id]["gender"], pets[pet_id]["color"])

def search_pets(pet_id: str = "", name: str = "", type: str = ""):
    print("Searching pets...")
    if pet_id != "":
        display_pet_profile_by_id(pet_id)
    elif name != "":
        try:
            with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
                pets = json.load(read_file)
            pet_list = []
            for pet_id in pets:
                if not pet_id.startswith("PT_"):
                    continue
                if pets[pet_id]["name"].lower() == name.lower():
                    pet_list.append(pet_id)
            if len(pet_list) < 1:
                input(f"No pets found matching the input name of '{name}'. Press Enter to continue...")
                return False
            for pet_id in pet_list:
                display_pet_profile_by_id(pet_id, "Short")
            return True
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "search_pets")
    elif type != "":
        try:
            with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
                pets = json.load(read_file)
            pet_list = []
            for pet_id in pets:
                if not pet_id.startswith("PT_"):
                    continue
                if pets[pet_id]["type"] == type:
                    pet_list.append(pet_id)
            if len(pet_list) < 1:
                input(f"No pets found matching the input type of '{type}'. Press Enter to return to Pet Profile Management...")
                return False
            for pet_id in pet_list:
                display_pet_profile_by_id(pet_id, "Short")
            return True
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "search_pets")


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
        for pet in range(len(pets) - 2):
            display_pet_profile_by_id(f"PT_{profile_id}", "short")
            profile_id += 1
    #TODO Need to run more testing on this function <-------------------


def validate_pet_entries():
    if not os.path.exists(TEST_FILE):
        generate_log(LogLevel.CRITICAL, "Unable to find JSON pet data file during validation of pet entries.", "validate_pet_entries")
        return
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
    except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "validate_pet_entries")
    
    pet_count = int(pets["total_entries"])
    num_pets = len(pets) -2
    if pet_count != num_pets:
        generate_log(LogLevel.WARNING, f"Entry count and pet profile count mis-match. Total entries was: {pet_count}, while number of pets is: {num_pets}!", "validate_pet_entries")
        pets["total_entries"] = num_pets
        try:
            with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(pets, write_file, indent=4)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "validate_pet_entries")
            return
    else:
        generate_log(LogLevel.INFO, "pets.json file integrity validated, no correction required.", "validate_pet_entries")


def create_pet_profile(pet: PetProfile):
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

    if len(pets["empty_slots"]) > 0:
        new_pet_id = pets["empty_slots"].pop(0)
    else:
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
            pet_count = int(pets["total_entries"])
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "delete_pet_profile_by_id")

    if pet_id in pets:
        print("Pet Found!")
        pet_to_remove = pets[pet_id]
        display_pet_profile_by_id(pet_id)
        confirm_delete = get_user_input(UserInput.CONFIRM_DELETE_PROFILE)
        if confirm_delete == "y" or confirm_delete == "yes":
            pets.pop(pet_id)
            new_pet_count = pet_count - 1
            pets["total_entries"] = new_pet_count
            pets["empty_slots"].append(pet_id)
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
        validate_pet_entries()

    else:
        print(f"Unable to find Pet ID: {pet_id}. Delete operation canceled!")
        input("Press Enter to continue...")

def edit_pet_profile_by_id(pet_id: str, pet: PetProfile):
    if not os.path.exists(TEST_FILE):
        generate_log(LogLevel.ERROR, f"File path to pets data does not exist. Unable to edit Pet ID: {pet_id}", "edit_pet_profile_by_id")
        raise Exception(f"ERROR: File path to pets data does not exist. Unable to edit Pet ID: {pet_id}")    
    try:
        with open(TEST_FILE, mode="r", encoding="utf-8") as read_file:
            pets = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "edit_pet_profile_by_id")
    updated_pet = {
        "name": pet.name,
        "type": pet.type,
        "age": pet.age,
        "gender": pet.gender,
        "color": pet.color
    }
    pets[pet_id] = updated_pet
    try:
        with open(TEST_FILE, mode="w", encoding="utf-8") as write_file:
            json.dump(pets, write_file, indent=4)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {TEST_FILE}: {e}", "delete_pet_profile_by_id")

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
            return PetProfile(name, type, age, gender, color)
        case UserInput.CONFIRM_DELETE_PROFILE:
            valid_input = ["y", "yes", "n", "no"]
            choice = input(text.value).lower()
            while choice not in valid_input:
                choice = input(text.value)
            return choice
        case UserInput.HAVE_PET_ID:
            valid_input = ["1", "2", "9"]
            choice = input(text.value).lower()
            while choice not in valid_input:
                choice = input(text.value)
            return int(choice)
        case UserInput.GET_PET_ID:
            choice = input(text.value)
            while not choice.isnumeric():
                choice = input(text.value)
            return f"PT_{choice}"
        case UserInput.SEARCH:
            valid_input = ["1", "2"]
            choice = input(text.value)
            while choice not in valid_input:
                choice = input(text.value)
            return int(choice)
        case UserInput.GET_PET_NAME:
            name = input(text.value)
            while not name:
                name = input(text.value)
            return name
        case UserInput.GET_PET_TYPE:
            type = input(text.value)
            while type not in [item.value for item in PetType]:
                type = input(text.value)
            return type
        case UserInput.EDIT_PETS:
            valid_input = ["1", "2", "3", "4", "5"]
            field_to_edit = input(text.value)
            while field_to_edit not in valid_input:
                field_to_edit = input(text.value)
            return int(field_to_edit)
        case UserInput.EDIT_PROFILE_NAME:
            text = input(text.value)
            if not text:
                text = input(text.value)
            return text
        case UserInput.EDIT_PROFILE_TYPE:
            type = input(text.value)
            if type not in [item.value for item in PetType]:
                type = input(text.value)
            return type
        case UserInput.EDIT_PROFILE_AGE:
            age = input(text.value)
            if not age.isnumeric():
                age = input(text.value)
            return age
        case UserInput.EDIT_PROFILE_GENDER:
            gender = input(text.value)
            if gender not in [item.value for item in PetGender]:
                gender = input(text.value)
            return gender
        case UserInput.EDIT_PROFILE_COLOR:
            color = input(text.value)
            if color not in [item.value for item in PetColor]:
                color = input(text.value)
            return color
        case _:
            generate_log(LogLevel.ERROR, "Function called without a valid UserInput enum", "get_user_input")

def display_valid_pet_genders():
    for line in GENDERS:
        print(GENDERS[line])

def display_valid_pet_types():
    for line in TYPES:
        print(TYPES[line])

def display_valid_pet_colors():
    for line in COLORS:
        print(COLORS[line])

def generate_log(level: LogLevel, log_message: str, func_name: str):
    #TODO: Have tempoarily added a truncate_limit constant to be used. This will need to be changed to use a settings.json file instead in the future. <-------------------
    if not os.path.exists(LOG_FILE):
        os.mkdir(LOG_FILE)
        
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
