user_password_dic = {"eva":"lösen123"}
user_items_dic = {"eva":[banan, blåbär, hallon]}

def start_page():
    print("Welcome to Lagra\n")
    print("l) Log in" + "\n" + "q) Quit" +"\n")
    chosen_option = input("Option: ")
    if chosen_option == "l":
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)
        
    return

def login(username, password):
    print( "hej")

def logout():
    return 

def add_to_list(ls, item):
    
    return

def escape():
    return

def main():
    start_page()
    
main()
