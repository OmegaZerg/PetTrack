import json
import os
from datetime import date
from functions import generate_log, get_user_input
from constants import *

def create_blog(blog_entry: str):
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    if not os.path.exists(BLOG_FILE):
        empty_blog = {formatted_date: None}
        try:
            with open(BLOG_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(empty_blog, write_file, indent=4)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "create_blog")
    try:
        with open(BLOG_FILE, mode="r", encoding="utf-8") as read_file:
            blogs = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "get_all_blogs")
        return
    if formatted_date in blogs:
        print(f"There is already a blog for today's date: '{formatted_date}'. Please use the edit menu to edit the existing blog instead.")
        return
    blogs[formatted_date] = blog_entry
    try:
        with open(BLOG_FILE, mode="w", encoding="utf-8") as write_file:
            json.dump(blogs, write_file, indent=4, sort_keys=True)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to write to {BLOG_FILE}: {e}", "get_all_blogs")

def edit_blog(date: str):
    pass

def menu_display_blog():
    blog = get_blogs("1")
    for key, value in blog.items():
        print(f"{key}: \n{value}\n")


def get_blogs(config: str, blog_date: str = ""):
    #TODO: Testing get_blogs function
    if not os.path.exists(BLOG_PATH):
        os.mkdir(BLOG_PATH)
    if not os.path.exists(BLOG_FILE):
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        empty_blog = {formatted_date: "Blog file has been created."}
        try:
            with open(BLOG_FILE, mode="w", encoding="utf-8") as write_file:
                json.dump(empty_blog, write_file, indent=4)
        except Exception as e:
            generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "get_all_blogs")
        return
    try:
        with open(BLOG_FILE, mode="r", encoding="utf-8") as read_file:
            blogs = json.load(read_file)
    except Exception as e:
        generate_log(LogLevel.ERROR, f"Unable to open {BLOG_FILE}: {e}", "get_pet_profile_by_id")
        return
    if len(blogs) < 1:
        generate_log(LogLevel.WARNING, f"Unable to get blogs. File '{BLOG_FILE}' is empty!")
        return
    
    if config == "by_date":
        if not blog_date:
            print("Blog ID is required when running the function 'get_blogs' with parameter of 'by_id' selected.")
            generate_log(LogLevel.ERROR, "Blog ID is required when running the function 'get_blogs' with parameter of 'by_id' selected. No Blog ID was supplied.", "get_blogs")
            return
        if blog_date in blogs:
            return f"Showing blog for date {blog_date}:\n{blogs[blog_date]}"
        return f"No blog found for date {blog_date}!"
    elif config == "all":
        return blogs
    elif config.isnumeric():
        num = int(config)
        last_num_blogs = dict(list(blogs.items())[-num:])
        return last_num_blogs