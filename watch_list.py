import pickle
from stock import stock

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
        self.ulist.append(stocks)
        print('Symbol: %s has been added to watchlist!' % ticker)

    def print_list(self):
        for stocks in self.ulist:
            print("%s: %f" % (stocks.get_ticker(), stocks.get_ask_price()))

    def update_list(self):
        try:
            with open('list_data.pkl', 'rb') as input:
                self.ulist = pickle.load(input)
        except IOError:
            print 'No tickers on watch!'

    def save_list(self):
        with open('list_data.pkl', 'wb') as output:
            pickle.dump(self.ulist, output, pickle.HIGHEST_PROTOCOL)
