import json
import os
from datetime import date
from functions import generate_log, get_user_input
from constants import *

def create_blog(blog_entry: str):
    pass

def edit_blog(date: str):
    pass

def menu_display_blog():
    top_blog = get_blogs("top_1") #Display the most recent blog on the menu
    pass

def get_blogs(config: str, blog_id: str = ""):
    #TODO: Testing get_blogs function
    if not os.path.exists(BLOG_PATH):
        os.mkdir(BLOG_PATH)
    if not os.path.exists(BLOG_FILE):
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        empty_blog = {formatted_date: None}
        try:
            with open(BLOG_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(empty_blog, write_file)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "get_all_blogs")
        return
    try:
        with open(BLOG_FILE, mode="r", encoding="utf-8") as read_file:
            blogs = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "get_pet_profile_by_id")
        return
    if len(blogs) < 3:
        return
    match config:
        case "top_1":
            #TODO: Return most recent blog
            print("Top1")
            pass
        case "all":
            #TODO: Return all blogs
            print("All")
            pass
        case "by_id":
            if not blog_id:
                print("Blog ID is required when running the function 'get_blogs' with parameter of 'by_id' selected.")
                return
            #TODO: Return the specific blog entry
            print("ID")
            pass

