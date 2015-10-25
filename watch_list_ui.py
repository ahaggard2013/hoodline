from watch_list import watch_list
import sys, os

class watch_list_ui:

    wl = None
    exit = None 

    def __init__(self):

        self.wl = watch_list()
        self.exit = False
        #######################
        ## MENUS DEFINITIONS ##
        #######################
        menu_actions = {
                        'main': self.main_menu,
                        '1': self.view_list,
                        '2': self.add_ticker,
                        '3': self.remove_ticker,
                        '4': self.back,}
        self.main_menu(menu_actions)

    def main_menu(self, menu_actions):
        os.system('clear')
        print('     1)  view list')
        print('     2)  add ticker')
        print('     3)  remove ticker')
        print('     4)  back')
        choice = raw_input('|>> ')
        self.run_menu(choice, menu_actions)

    def run_menu(self, choice, menu_actions):
        if choice == '':
            menu_actions['main'](menu_actions)
        else:
            try:
                menu_actions[choice]()
                if self.exit is False:
                    menu_actions['main'](menu_actions)
            except KeyError:
                print('Invalid Selection: %s' % choice)
                menu_actions['main'](menu_actions)
        return
    
    def view_list(self):
       self.wl.print_list()

    def add_ticker(self):
        ticker = raw_input('enter ticker to add: ')
        if (ticker == ''):
            return
        self.wl.add_ticker(ticker)
        self.wl.save_list()

    def remove_ticker(self):
        ticker = raw_input('enter ticker to remove: ')
        if (ticker == ''):
            return
        self.wl.remove_ticker(ticker)
        self.wl.save_list()
        
    def back(self):
        self.exit = True
