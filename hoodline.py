from Robinhood import Robinhood
import getpass
from main_ui import main_ui

def login():
    username = raw_input('Login: ')
    password = getpass.getpass('Password: ')
    trader = Robinhood()
    login_check = trader.login(username, password)
    if login_check is False:
        print 'Error: Wrong Email or Password'
        sys.exit(0)
    return trader

def menu():
    ui = main_ui()

def main():
    trader = login()
    menu()
    


if __name__ == "__main__":
        main()
