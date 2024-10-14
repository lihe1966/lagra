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

def main():
    splash()
    start_page()

def splash():
    print("\nWelcome to Lagra (TM) \n")

def start_page():
    print("l) Log in" + "\n" + "q) Quit" +"\n")
    chosen_option = input("Option: ")
    if chosen_option == "l":
        login()
    elif chosen_option == "q":
        shutdown()
    else:
        while not chosen_option == "l" and not chosen_option == "q":
            print("Please enter valid option.")
            chosen_option = input("Option: ")
        if chosen_option == "l":
            login()
        elif chosen_option == "q":
            shutdown()  

def shutdown():
    print("Lagra shutting down.")
    exit()

def login():
    username = input("\nUsername: ")
    password = input("\nPassword: ")
    authentication(username, password)
    
def authentication(username, password):
    if username in user_password_dic:
        if user_password_dic[username] == password:
            item_page(username)
        else:
            try_again()
    else:
        try_again()
    
def try_again():
    print("Invalid username or password.")
    print("\n r) Try again \n q) Quit \n")
    chosen_option = input("Option: ")
    if chosen_option == "r":
        login()
    elif chosen_option == "q":
        shutdown()
    else:
        while not chosen_option == "r" or chosen_option =="q":
            print("Please enter valid option.")
            chosen_option = input("Option: ")

def item_page(username): 
    item_list = user_items_dic[username]
    item_count = 1
    print ("\nThese are your items.\n")
    for i in item_list:
        print (f"{item_count}) {i}")
        item_count += 1
    item_page_options(username)

def item_page_options(username):
    print ("\nSelect an action. \n \na) Add item \nl) List items \nq) Log out \n")
    chosen_option = input("Option: ")
    if chosen_option == "a":
        add_to_list(user_items_dic[username], input("\nAdd an item: "))
        item_page(username)
    elif chosen_option == "l":
        item_page(username)
    elif chosen_option == "q":
        main()
    else:
        print("Please enter valid option.")
        item_page_options(username)        

def add_to_list(ls, item):
    ls.append(item)
