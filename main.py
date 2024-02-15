import os as sys
import time as t
import webbrowser
import pyfiglet

notes = [

]
def documentation():
    webbrowser.open("https://youtube.com")
def project_webiste():
    webbrowser.open("https://youtube.com")

def add_notes():
    x = input("what note add? >>")
    notes.append(x)
def read_notes():
    for i in range(len(notes)):
        print(f"note number  {i}:  {notes[i]}")

def get_disk_usage():
    """
    Get disk usage statistics for the root path and print the information.
    """
    try:
        import psutil
    except ImportError:
        print("Error: psutil module not found. Please install it using 'pip install psutil'.")
        return

    disk_usage = psutil.disk_usage('/')
    print("Disk Usage Information:")
    print(f"Total: {disk_usage.total} bytes")
    print(f"Used: {disk_usage.used} bytes")
    print(f"Free: {disk_usage.free} bytes")
    print(f"Usage Percentage: {disk_usage.percent}%")

def get_running_processes():
    try:
        import psutil
    except ImportError:
        print("Error: psutil module not found. Please install it using 'pip install psutil'.")
        return

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        process_info = {
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'username': proc.info['username'],
            'cpu_percent': proc.info['cpu_percent'],
            'memory_percent': proc.info['memory_percent']
        }
        processes.append(process_info)
    
    print("Running Processes:")
    for process in processes:
        print(f"PID: {process['pid']}, Name: {process['name']}, Username: {process['username']}, CPU%: {process['cpu_percent']}, Memory%: {process['memory_percent']}")


logins = {
    "admin": ["1234", True, 1],
    "user": ["1234pass", False, 2]
}

clear_screen = lambda: sys.system('cls')

def succ_command():
    global count
    count = 0


count = 0
nxt_id = 3
def add_user():
    global logins, count, nxt_id
    user_input = input("Enter new user name >>").lower()
    if user_input != "break":
        password_input = input("Enter password >>")
        if password_input != "break":
            privilege_input = input("Enter admin privileges (True/False) >>").lower()
            if privilege_input != "break":
                privilege = True if privilege_input == "true" else False
                logins[user_input] = [password_input, privilege, nxt_id]
                nxt_id += 1
                print("User added successfully!")
            else:
                print("Add user command ended")
        else:
            print("Add user command ended")
    else:
        print("Add user command ended")

def drop_user():
    user_id = int(input("   what user to drop (id)>>"))
    for name, details in logins.items():
        if details[2] == user_id:
            del logins[name]
            print("User dropped successfully!")
            return
    print("User with specified ID not found.")


def check_users():
    for name, details in logins.items():
        print("Name:", name)
        print("Password:", details[0])
        print("Is admin:", details[1])
        print("ID:", details[2])

import random as r
random_nr = lambda: print(r.randint(1, 10))

def delogin():
    global usr_login, usr_pass
    usr_login = False
    usr_pass = False

def quit():
    global run
    run = False

def show_commands():
    for key in commands:
        print(key)


commands = {
    'help()': show_commands,
    'add_user()': add_user,
    'clear_screen()': clear_screen, #<= Lambda
    #'log_out()': logout,
    'drop_user()': drop_user,
    'check_users()':check_users,
    'random_nr()':random_nr, #<= Lambda,
    'quit()':quit,
    'disk_usage()': get_disk_usage,
    'running_proceses()':get_running_processes,
    'add_note()':add_notes,
    'read_notes()':read_notes,
    'documentation()':documentation
}

# login system
def login_sys(user_login_input, user_password_input):
    user_login_input = user_login_input.lower()
    for username, password in logins.items():
        if user_login_input == username:
            if user_password_input == password[0]:
                return True
    return False

def main_loop():
    global count, usr_login, usr_pass
    while usr_login and usr_pass:  # Check if user is logged in
        count += 1
        user_input = input(f"   {count}>>")
        if user_input in commands:
            commands[user_input]()
            succ_command()
        elif user_input == "logout":  # Check if the user wants to log out
            delogin()  # Log out the user
            print("Logged out successfully!")
            break  # Breakbe out of the loop after logging out
        else:
            print("=wrong command=")
        for i in range(1):
            print("")

run = True
while run:
    login_access = False
    password_access = False
    usr_login = input(f"{count} login>>")
    count += 1
    usr_pss = input(f"{count} password>>")
    if login_sys(usr_login, usr_pss):
        print(f"Logged as: {usr_login}")
        t.sleep(1)
        clear_screen()
        t.sleep(0.1)
        print("=================================")
        print(pyfiglet.figlet_format("Pi COS", font="slant"))
        t.sleep(0.1)
        print("=================================")
        t.sleep(0.1)
        usr_pass = True
        main_loop()
        succ_command() 
    else:
        print("Access denied! Wrong username or password.")
