import pickle
from stock import stock
from bcolors import bcolors

###############################################
##Stores stocks in a list for you to referece##
###############################################


class watch_list:

    ulist = []

    def __init__(self):
        self.update_list()

    def add_ticker(self, ticker):
        stocks = stock(ticker)
        if stocks.valid is False:
            return False
        if self.in_list(stocks):
            print('Symbol: %s is already in your list!' % ticker)
            raw_input("Press Enter to continue...")
            return False
        self.ulist.append(stocks)
        print('Symbol: %s has been added to watchlist!' % ticker)
        raw_input("Press Enter to continue...")

    def remove_ticker(self, ticker):
        for stocks in self.ulist:
            if (ticker == stocks.get_ticker()):
                self.ulist.remove(stocks)
                print('Symbol: %s has been removed from  watchlist!' % ticker)
                raw_input("Press Enter to continue...")
                return True
        print('Symbol: %s is not in watchlist!' % ticker)
        raw_input("Press Enter to continue...")

    def print_list(self):
        color = bcolors()
        for stocks in self.ulist:
            ask_price = stocks.get_ask_price()
            close = stocks.get_prev_close()
            if (ask_price > close):
                print("%s: Price: %s%.2f (%.2f%%)%s" % (stocks.get_ticker(), color.OKGREEN, ask_price, (((ask_price - close) / close) * 100),color.ENDC))
            else: 
                print("%s: Price: %s%.2f (%.2f%%)%s" % (stocks.get_ticker(), color.FAIL, ask_price, (((ask_price - close) / close) * 100),color.ENDC))
        raw_input("Press Enter to continue...")

    def update_list(self):
        try:
            with open('list_data.pkl', 'rb') as input:
                self.ulist = pickle.load(input)
        except IOError:
            print 'No tickers on watch!'

    def save_list(self):
        with open('list_data.pkl', 'wb') as output:
            pickle.dump(self.ulist, output, pickle.HIGHEST_PROTOCOL)

    def in_list(self, stock_check):
        for stocks in self.ulist:
            if (stocks.get_ticker() == stock_check.get_ticker()):
                return True
        return False
