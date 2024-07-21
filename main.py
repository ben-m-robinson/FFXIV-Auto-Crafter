import customtkinter
import time
import pyautogui
from configparser import ConfigParser

pyautogui.pause = 2.5
pyautogui.FAILSAFE = True

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

file = "config.ini"
config = ConfigParser()
config.read(file)

total_crafts = 0
macro_1Button = config.get("keyBinds", "macro_1Button")
macro_2Button = config.get("keyBinds", "macro_2Button")
confirm_Keybind = config.get("keyBinds", "confirm_keybind")
ui_Cycle_Keybind = config.get("keyBinds", "ui_cycle_keybind")
recipe_Name = ""

def submit():
    global macro_1Button
    global macro_2Button
    global confirm_Keybind
    global ui_Cycle_Keybind

    config = ConfigParser()
    config.read(file) 
    cnfFile = open(file, "w")
    config.set("keyBinds","macro_1Button",entry1.get())
    config.set("keyBinds","macro_2Button",entry2.get())
    config.set("keyBinds","confirm_keybind",entry4.get())
    config.set("keyBinds","ui_Cycle_Keybind",entry5.get())
    config.write(cnfFile)
    cnfFile.close()

    macro_1Button = config.get("keyBinds", "macro_1Button")
    macro_2Button = config.get("keyBinds", "macro_2Button")
    confirm_Keybind = config.get("keyBinds", "confirm_keybind")
    ui_Cycle_Keybind = config.get("keyBinds", "ui_cycle_keybind")

def locate_search():
    global recipe_Name
    recipe_Name = entry6.get()

    pyautogui.press("n")
    i = 0
    while i < 10:
        pyautogui.press(ui_Cycle_Keybind)
        i += 1
    pyautogui.press(confirm_Keybind)          
    pyautogui.write(recipe_Name)
    pyautogui.press("enter")
    time.sleep(2.5)
    pyautogui.press(confirm_Keybind)  

def craft():
    global total_crafts
    total_crafts = int(entry3.get())


    time.sleep(10)
    locate_search()
    count = 0
    while count < total_crafts:
        pyautogui.press(confirm_Keybind) 
        time.sleep(1)
# press 1st macro button
        pyautogui.press(macro_1Button)
        if(len(macro_2Button) > 0):
            time.sleep(45)
        else: time.sleep(80)

# press 2nd macro button
        if(len(macro_2Button) > 0):
            pyautogui.press(macro_2Button)
            time.sleep(25)
            pyautogui.press(confirm_Keybind)
        count+=1
    

root = customtkinter.CTk()
root.geometry("500x400")

label = customtkinter.CTkLabel(master=root, text="FFXIV Auto Crafter", font = ("Times", 24))
label.pack(pady=12, padx=10)

my_tab = customtkinter.CTkTabview(root)
my_tab.pack(pady=10)

homeTab = my_tab.add("Home")
settingsTab = my_tab.add("Settings")


entry1 = customtkinter.CTkEntry(master=settingsTab, width = 330, placeholder_text="Enter the keybind for the first macro")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=settingsTab, width = 330, placeholder_text="Enter the keybind for the second macro")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=homeTab, width = 330, placeholder_text="Enter the number of crafts you would like to perform")
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=settingsTab, width = 330, placeholder_text="Enter 'confirm' keybind")
entry4.pack(pady=12, padx=10)

entry5 = customtkinter.CTkEntry(master=settingsTab, width = 330, placeholder_text="Enter 'cycle through ui' keybind")
entry5.pack(pady=12, padx=10)

entry6 = customtkinter.CTkEntry(master=homeTab, width = 330, placeholder_text="Enter the name of the item to craft")
entry6.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=settingsTab, width = 150, height = 30, text = "Submit", command = submit)
button.pack(padx=20, pady=10)

button = customtkinter.CTkButton(master=homeTab, width = 150, height = 30, text = "Run", command = craft)
button.pack(padx=20, pady=10)

root.mainloop()