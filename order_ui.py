import sys, os
from threading import Thread
from order import order
class orders_ui:

    ol = None
    exit = None

    def __init__(self):
        self.exit = False
        menu_actions = {
                        'main': self.main_menu,
                        '1': self.market_order,}
        self.main_menu(menu_actions)

    def main_menu(self, menu_actions):
        os.system('clear')
        print('     1)  Market Order')
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

    def market_order(self):
        morder = order()
