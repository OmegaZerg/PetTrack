from functions import *
from constants import *

def main():
    print("~~~~~~~~~~~~| Hello from Pet-Track! |~~~~~~~~~~~~")
    #TODO: display existing profiles here (maximum of like 5?)
    menu_choice = get_user_input(UserInput.MAIN_MENU)
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
            

    display_pet_profile_by_id("PT_1")

    print("Testing create_pet_profile")
    create_pet_profile("Lucky", "Dog", 2, "M", "Black")

    print("Testing delete_pet_profile_by_id")
    delete_pet_profile_by_id("PT_6")

if __name__ == "__main__":
    main()