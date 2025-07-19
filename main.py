from functions import *
from constants import *
import os

def main():
    
    #Check settings


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("~~~~~~~~~~~~| Hello from Pet-Track! |~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~| Main Menu |~~~~~~~~~~~~~~~~~~~")
        #TODO: display existing profiles here (maximum of like 5?)
        menu_choice = get_user_input(UserInput.MAIN_MENU)
        print(f"You chose: {menu_choice}")

        match menu_choice:
            case 1:
                #Function for option 1 - View/Manage Pet Profile
                os.system('cls' if os.name == 'nt' else 'clear')
                print("~~~~~~~~~~~~| Pet Profile Management |~~~~~~~~~~~~")
                sub_menu_choice = get_user_input(UserInput.MANAGE_PETS_MENU)
                match sub_menu_choice:
                    case 1:
                        #Function for View Existing
                        pass
                    case 2:
                        #Function for Edit Existing
                        pass
                    case 3:
                        #Function for Creating New Profile
                        
                        create_pet_profile()
                    case 9:
                        #Return to main menu
                        continue
                    case _:
                        raise ValueError(f"Unknown input of {menu_choice} was provided for the View/Manage Pet profile menu.")
            case 2:
                #Function for option 2 - Food Logging
                pass
            case 3:
                #Function for option 3 - Reminders
                pass
            case 4:
                #Function for option 4 - Blog
                pass
            case 9:
                print("Closing Pet_Track.")
                break
            case _:
                raise ValueError(f"Unknown input of {menu_choice} was provided for the main menu.")
            

    print("Testing create_pet_profile")
    create_pet_profile("Lucky", "Dog", 2, "M", "Black")

    print("Testing delete_pet_profile_by_id")
    delete_pet_profile_by_id("PT_2")

if __name__ == "__main__":
    main()