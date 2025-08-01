from functions import *
from blog_functions import *
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
            case 1:
                while True:
                    #Main Menu option 1 - View/Manage Pet Profile
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{MenuHeader.PROF_MGMNT_1.value:{"~"}^50}")
                    print(f"{MenuHeader.PROF_MGMNT_2.value:{"~"}^50}")
                    print()
                    menu_display_pet_profiles(3)
                    print()
                    sub_menu_choice = get_user_input(UserInput.MANAGE_PETS)
                    match sub_menu_choice:
                        case 1:
                            #View
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.VIEW_1.value:{"~"}^50}")
                            have_pet_id = get_user_input(UserInput.HAVE_PET_ID)
                            match have_pet_id:
                                case 1:
                                    pet_id = get_user_input(UserInput.GET_PET_ID)
                                    display_pet_profile_by_id(pet_id)
                                    input("Press Enter to continue...")
                                case 2:
                                    search_method = get_user_input(UserInput.SEARCH)
                                    match search_method:
                                        case 1:
                                            pet_name = get_user_input(UserInput.GET_PET_NAME)
                                            pet_id_found = search_pets(name = pet_name)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the name '{pet_name}'. Please make note of the Pet profile ID you wish to edit, then continue back through the edit process. Press Enter to continue...")
                                            continue
                                        case 2:
                                            print("Valid Pet Types:")
                                            for line in TYPES:
                                                print(TYPES[line])
                                            pet_type = get_user_input(UserInput.GET_PET_TYPE)
                                            pet_id_found = search_pets(type = pet_type)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the type '{pet_type}'. Please make note of the Pet profile ID you wish to edit, then continue back through the edit process. Press Enter to continue...")
                                            continue
                                        case _:
                                            raise ValueError(f"Unknown input of {search_method} was provided for the Search Pet profile menu.")    
                                case 9:
                                    continue
                        case 2:
                            #Edit
                            #TODO: edit menu needs more testing
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.EDIT_1.value:{"~"}^50}")
                            have_pet_id = get_user_input(UserInput.HAVE_PET_ID)
                            match have_pet_id:
                                case 1:
                                    pet = None
                                    while not pet:
                                        pet_id = get_user_input(UserInput.GET_PET_ID)
                                        pet = get_pet_profile_by_id(pet_id)
                                    print(f"Selected {pet}")
                                    field_to_edit = get_user_input(UserInput.EDIT_PETS)
                                    match field_to_edit:
                                        case 1:
                                            #Name
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            display_pet_profile_by_id(pet_id)
                                            print(f"Editing Name for Pet Profile '{pet_id}'. ", end="")
                                            updated_name = get_user_input(UserInput.EDIT_PROFILE_NAME)
                                            pet.name = updated_name
                                            print(f"Updated pet: {pet}")
                                            edit_pet_profile_by_id(pet_id, pet)
                                        case 2:
                                            #Type
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            display_valid_pet_types()
                                            display_pet_profile_by_id(pet_id)
                                            print(f"Editing Type for Pet Profile '{pet_id}'. ", end="")
                                            updated_type = get_user_input(UserInput.EDIT_PROFILE_TYPE)
                                            pet.type = updated_type
                                            print(f"Updated pet: {pet}")
                                            edit_pet_profile_by_id(pet_id, pet)
                                        case 3:
                                            #Age
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            display_pet_profile_by_id(pet_id)
                                            print(f"Editing Age for Pet Profile '{pet_id}'. ", end="")
                                            updated_age = get_user_input(UserInput.EDIT_PROFILE_AGE)
                                            pet.age = updated_age
                                            print(f"Updated pet: {pet}")
                                            edit_pet_profile_by_id(pet_id, pet)
                                        case 4:
                                            #Gender
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            display_valid_pet_genders()
                                            display_pet_profile_by_id(pet_id)
                                            print(f"Editing Gender for Pet Profile '{pet_id}'. ", end="")
                                            updated_gender = get_user_input(UserInput.EDIT_PROFILE_GENDER)
                                            pet.gender = updated_gender
                                            print(f"Updated pet: {pet}")
                                            edit_pet_profile_by_id(pet_id, pet)
                                        case 5:
                                            #Color
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            display_valid_pet_colors()
                                            display_pet_profile_by_id(pet_id)
                                            print(f"Editing Color for Pet Profile '{pet_id}'. ", end="")
                                            updated_color = get_user_input(UserInput.EDIT_PROFILE_COLOR)
                                            pet.color = updated_color
                                            print(f"Updated pet: {pet}")
                                            edit_pet_profile_by_id(pet_id, pet)
                                    input("Press Enter to continue...")
                                case 2:
                                    search_method = get_user_input(UserInput.SEARCH)
                                    match search_method:
                                        case 1:
                                            pet_name = get_user_input(UserInput.GET_PET_NAME)
                                            pet_id_found = search_pets(name = pet_name)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the name '{pet_name}'. Press Enter to continue...")
                                            continue
                                        case 2:
                                            print("Valid Pet Types:")
                                            for line in TYPES:
                                                print(TYPES[line])
                                            pet_type = get_user_input(UserInput.GET_PET_TYPE)
                                            pet_id_found = search_pets(type = pet_type)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the type '{pet_type}'. Press Enter to continue...")
                                            continue
                                        case _:
                                            raise ValueError(f"Unknown input of {search_method} was provided for the Search Pet profile menu.")    
                                case 9:
                                    continue
                        case 3:
                            #Create
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.CREATE_1.value:{"~"}^50}")
                            print(f"{MenuHeader.CREATE_2.value:{"~"}^50}")
                            display_valid_pet_genders()
                            display_valid_pet_types()
                            display_valid_pet_colors()
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
                                            pet_id_found = search_pets(name = pet_name)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the name '{pet_name}'. Please note the Pet Profile ID of the pet you wish to delete, then continue back through the deletion process. Press Enter to return continue...")
                                            continue
                                        case 2:
                                            print("Valid Pet Types:")
                                            for line in TYPES:
                                                print(TYPES[line])
                                            pet_type = get_user_input(UserInput.GET_PET_TYPE)
                                            pet_id_found = search_pets(type = pet_type)
                                            if pet_id_found:
                                                input(f"\nShowing all pets with the type '{pet_type}'. Please note the Pet Profile ID of the pet you wish to delete, then continue back through the deletion process. Press Enter to continue...")
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
                            raise ValueError(f"Unknown input of {sub_menu_choice} was provided for the View/Manage Pet profile menu.")
            case 2:
                #Main Menu option 2 - Food Logging
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{MenuHeader.FOOD_LOG_1.value:{"~"}^50}")
                print("Food Logging Feature coming soon!")
                input("Press Enter to continue...")
            case 3:
                #Main Menu option 3 - Reminders
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{MenuHeader.REMINDERS_1.value:{"~"}^50}")
                print("Pet Reminders Feature coming soon!")
                input("Press Enter to continue...")
            case 4:
                #Main Menu option 4 - Blog
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{MenuHeader.BLOG_1.value:{"~"}^50}")
                    print(f"{MenuHeader.BLOG_2.value:{"~"}^50}")
                    menu_display_blog()
                    sub_menu_choice = get_user_input(UserInput.BLOGS)
                    match sub_menu_choice:
                        case 1:
                            #TODO: View Blogs
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{MenuHeader.BLOG_VIEW.value:{"~"}^50}")
                            view_choice = get_user_input(UserInput.BLOG_VIEW)
                            match view_choice:
                                case 1:
                                    #TODO: View All
                                    input("View All")
                                    get_blogs("all")
                                    pass
                                case 2:
                                    #TODO: View top n
                                    input("View top n")
                                    pass
                                case 3:
                                    #TODO: View by date
                                    input("View by date")
                                    pass
                                case 9:
                                    #Return to Blogs Menu
                                    continue
                            pass
                        case 2:
                            #TODO: Edit Blogs
                            pass
                        case 3:
                            #TODO: Create Blogs
                            #TODO: Need input to gather the blog text
                            create_blog("This is a test")
                            pass
                        case 9:
                            #Return to main menu
                            break
                        case _:
                            raise ValueError(f"Unknown input of {sub_menu_choice} was provided for the Blog menu.")
                    input("Press Enter to continue...")
            case 9:
                print("Closing Pet_Track.")
                break
            case _:
                raise ValueError(f"Unknown input of {menu_choice} was provided for the main menu.")
            

if __name__ == "__main__":
    main()