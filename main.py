from tkinter import *
import customtkinter


"""
Creates the main window for the task manager application using Tkinter and CustomTkinter.
"""
# window
root = customtkinter.CTk()
root.title("Tasks manager")
root.geometry("450x450+750+250")
root.resizable(False, False)
root.iconbitmap("icons/icon.ico")
# set dark mode
customtkinter.set_appearance_mode("dark")


"""
Defines functions for adding, removing, clearing, saving, and loading tasks.
"""
# functions
def add_task():
    # Adds a new task to the list
    list_box.insert(END, f"{id_input.get()} {user_input.get()}")
    user_input.delete(0, END)
    id_input.delete(0, END)


def remove_task():
    # Removes the selected task from the list
    list_box.delete(ANCHOR)


def clear_all_tasks():
    # Clears all tasks from the list
    list_box.delete(0, END)


def save_task_list():
    # Saves all tasks to a text file
    with open("tasks.txt", "w", encoding="utf-8") as my_file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                my_file.write(f"{one_task}")
            else:
                my_file.write(f"{one_task}\n")


def open_tasks_file():
    # Loads tasks from a text file at startup
    try:
        with open("tasks.txt", "r", encoding="utf-8") as my_file:
            for one_task in my_file:
                list_box.insert(END, one_task)
    except FileExistsError:
        print("Error. Cannot find file with tasks.")


"""
Defines fonts, colors, and padding for the UI elements.
"""
# fonts, colors, padding
main_font = ("Verdana", 10)
main_color = "#dd7f00"
button_color = "#ffbe66"

"""
Creates frames for input, text display, and buttons.
"""
# Frames
input_frame = customtkinter.CTkFrame(root)
text_frame = customtkinter.CTkFrame(root)
button_frame = customtkinter.CTkFrame(root)
input_frame.pack(padx=2, pady=2)
text_frame.pack(padx=2, pady=2)
button_frame.pack(padx=2, pady=2)

"""
Creates input fields for task ID and task description, and an "Add task" button.
"""
# input frame
id_input = customtkinter.CTkEntry(input_frame,
                                  width=80, placeholder_text=f"Type id: '1.'")
id_input.grid(row=0, column=0, padx=4, pady=4, sticky="ew")
user_input = customtkinter.CTkEntry(input_frame, placeholder_text="Type your task...",
                                    width=250)
user_input.grid(row=0, column=1, padx=4, pady=4, sticky="ew")
add_item = customtkinter.CTkButton(input_frame, text="Add task", width=10,
                                   hover_color=(button_color, main_color),
                                   border_width=1, command=add_task)
add_item.grid(row=0, column=2, padx=4, pady=4, ipadx=1)

"""
Creates a listbox for displaying tasks and scrollbars for navigation.
"""
# text frame
list_box = Listbox(text_frame, width=49, height=14, selectborderwidth=3, font=main_font)
list_box.grid(row=0, column=0, sticky="nsew")

## vertical listbox scrollbar
vertical_scrollbar = customtkinter.CTkScrollbar(text_frame, button_hover_color=(button_color, main_color),
                                                command=list_box.yview)
vertical_scrollbar.grid(row=0, column=1, sticky="ns")

## horizontal listbox scrollbar
horizontal_scrollbar = customtkinter.CTkScrollbar(text_frame, button_hover_color=(button_color, main_color),
                                                  command=list_box.xview, orientation="horizontal")
horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

## connect list_box to vertical scrollbar
list_box.configure(yscrollcommand=vertical_scrollbar.set)

## connect list_box to horizontal scrollbar
list_box.configure(xscrollcommand=horizontal_scrollbar.set)

"""
Creates buttons for removing a task, clearing the list, saving the list, and quitting the application.
"""
# button frame
remove_item = customtkinter.CTkButton(button_frame, text="Remove task", width=25, border_width=1,
                                      command=remove_task)
clear_list = customtkinter.CTkButton(button_frame, text="Clear list", width=25, border_width=1,
                                     command=clear_all_tasks)
save_list = customtkinter.CTkButton(button_frame, text="Save list", width=25, border_width=1,
                                    command=save_task_list)
quit_app = customtkinter.CTkButton(button_frame, text="Quit", width=25, border_width=1,
                                   command=root.destroy)
remove_item.grid(row=0, column=0, padx=11, pady=8, ipadx=10)
clear_list.grid(row=0, column=1, padx=11, pady=8, ipadx=10)
save_list.grid(row=0, column=2, padx=11, pady=8, ipadx=10)
quit_app.grid(row=0, column=3, padx=11, pady=8, ipadx=10)

"""
Loads tasks from a text file and inserts them into the list_box widget.
It is called to fill the list_box with tasks stored in a text file 
when the application starts.
"""
# insert all saved tasks to list_box
open_tasks_file()

"""
Starts the main event loop of the Tkinter application and handles it as long as the window is open. 
"""
# main cycle
root.mainloop()
