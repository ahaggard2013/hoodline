import watch_list
from watch_list_ui import watch_list_ui
import sys, os


class main_ui:

    def __init__(self):
        #######################
        ## MENUS DEFINITIONS ##
        #######################
        menu_actions = {
                        'main': self.main_menu,
                        '1': watch_list_ui,
                        '2': self.exit,}
        self.main_menu(menu_actions)

    def main_menu(self, menu_actions):
        os.system('clear')
        print('     1)  watch list')
        print('     2)  exit')
        choice = raw_input('|>> ')
        self.run_menu(choice, menu_actions)

    def exit(self):
        sys.exit(0)

    def run_menu(self, choice, menu_actions):
        if choice == '':
            menu_actions['main'](menu_actions)
        else:
            try:
                menu_actions[choice]()
                menu_actions['main'](menu_actions)
            except KeyError:
                print('Invalid Selection: %s' % choice)
                menu_actions['main'](menu_actions)
        return
