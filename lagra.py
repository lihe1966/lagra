user_password_dic = {
    "eva":"lösen123",
    "sven":"sten100",
    "kalle":"anka",
    "lisa":"ethernet"
    }
user_items_dic = {
    "eva":["banan", "blåbär", "hallon"],
    "sven":["granit", "marmor", "kalksten"],
    "kalle":["mussepigg", "farbroranka"],
    "lisa":["tangentbord", "mus", "skärm"]
    }

def start_page():
    print("Welcome to Lagra\n")
    print("l) Log in" + "\n" + "q) Quit" +"\n")
    chosen_option = input("Option: ")
    if chosen_option == "l":
        login()
    elif chosen_option == "q":
        print("Program shutting down.")
        exit()
    else:
        while not chosen_option == "l" or chosen_option =="q":
            print("Please enter valid option.")
            chosen_option = input("Option: ")
    return

def item_page(username): 
    item_list = user_items_dic[username]
    item_count = 1
    print ("These are your items. \n")
    for i in item_list:
        print (f"{item_count}) {i}")
        item_count += 1
    options(username)

def login():
    username = input("Username: ")
    password = input("Password: ")
    authentication(username, password)
    
def authentication(username, password):
    if username in user_password_dic:
        if user_password_dic[username] == password:
            item_page(username)
            return
        else:
            try_again()
            return
    else:
        try_again()
        return
    
def options(username):
    print ("\n Select an action. \n \n a) Add item \n l) List items \n q) Log out")
    chosen_option = input("Option: ")
    if chosen_option == "a":
        add_to_list(user_items_dic[username], input("Add an item: "))
        item_page(username)
    elif chosen_option == "l":
        item_page(username)
    elif chosen_option == "q":
        start_page()
        
def try_again():
    print("Invalid username or password.")
    print("\n r) Try again \n q) Quit \n")
    chosen_option = input("Option: ")
    if chosen_option == "r":
        login()
    elif chosen_option == "q":
        print("Program shutting down.")
        exit()
    else:
        while not chosen_option == "r" or chosen_option =="q":
            print("Please enter valid option.")
            chosen_option = input("Option: ")
    return

def logout():
    return 

def add_to_list(ls, item):
    ls.append(item)
    return

def main():
    start_page()
    
#main()

