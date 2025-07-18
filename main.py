from functions import *
from constants import *
import json

def main():
    print("~~~~~~~~~~~~| Hello from Pet-Track! |~~~~~~~~~~~~")
    #TODO: display existing profiles here (maximum of like 5?)
    menu_choice = get_user_input(MAIN_MENU)
    print(f"You chose: {menu_choice}")

    match menu_choice:
        case 1:
            #Function for option 1
            pass
        case 2:
            #Function for option 2
            pass
        case 3:
            #Function for option 3
            pass
        case _:
            #Unknown input
            raise ValueError(f"Unknown input of {menu_choice} was provided.")
            
    with open("pets.json", mode="r", encoding="utf-8")  as read_file:
        pets = json.load(read_file)
    
    print("This is printing the pets file:\n")
    print(pets)
    print(f"Total entries: {pets["total_entries"]}")
    #print(f"First pet: {pets["PT_1"]}")
    get_pet_profile_by_id("PT_1")

if __name__ == "__main__":
    main()