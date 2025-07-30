from functions import *
from constants import *
import os

def main():
    #TODO: Potentially add setting.json file to store user configured settings of the app? <-------------------
    #Check settings func

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{MenuHeader.MAIN_1.value:{"~"}^50}")
        print(f"{MenuHeader.MAIN_2.value:{"~"}^50}")
        menu_choice = get_user_input(UserInput.MAIN_MENU)

        match menu_choice:
            #Pet Management
            case 1:
                while True:
                    #Main Menu option 1 - View/Manage Pet Profile
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{MenuHeader.PROF_MGMNT.value:{"~"}^50}")
                    print(f"{MenuHeader.PROF_MGMNT_2.value:{"~"}^50}")
                    print()
                    menu_display_pet_profiles(3)
                    print()
                    sub_menu_choice = get_user_input(UserInput.MANAGE_PETS)
                    match sub_menu_choice:
                        case 1:
                            #Function for View Existing
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.VIEW_1.value:{"~"}^50}")
                            #TODO: Build menu/options
                            input("Press Enter to continue...")
                        case 2:
                            #Function to Edit Existing
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.EDIT_1.value:{"~"}^50}")
                            #TODO: Build menu/options
                            input("Press Enter to continue...")
                        case 3:
                            #Create
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.CREATE_1.value:{"~"}^50}")
                            print(f"{MenuHeader.CREATE_2.value:{"~"}^50}")
                            display_valid_pet_inputs()
                            temp_pet_object = get_user_input(UserInput.CREATE_PROFILE)
                            create_pet_profile(temp_pet_object)
                            input("New profile created successfully. Press Enter to continue...")
                        case 4:
                            #Delete
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.DELETE_1.value:{"~"}^50}")
                            have_pet_id = get_user_input(UserInput.HAVE_PET_ID)
                            match have_pet_id:
                                case 1:
                                    pet_id = get_user_input(UserInput.GET_PET_ID)
                                case 2:
                                    search_method = get_user_input(UserInput.SEARCH)
                                    match search_method:
                                        case 1:
                                            pet_name = get_user_input(UserInput.GET_PET_NAME)
                                            #Currently not returning anything, sending back to menu instead
                                            pet_id = search_pets(name = pet_name)
                                            continue
                                        case 2:
                                            print("Valid Pet Types:")
                                            for line in TYPES:
                                                print(TYPES[line])
                                            pet_type = get_user_input(UserInput.GET_PET_TYPE)
                                            #Currently not returning anything, sending back to menu instead
                                            pet_id = search_pets(type = pet_type)
                                            continue
                                        case _:
                                            raise ValueError(f"Unknown input of {search_method} was provided for the Search Pet profile menu.")    
                                case 9:
                                    continue
                            delete_pet_profile_by_id(pet_id)
                        case 9:
                            #Return to main menu
                            break
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
            

if __name__ == "__main__":
    main()