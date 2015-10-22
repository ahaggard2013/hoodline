import pickle
from stock import stock

###############################################
##Stores stocks in a list for you to referece##
###############################################


class watch_list:

    list = []

    def __init__(self):
        try:
            with open('list_data.pkl', 'rb') as input:
                while True:
                    try:
                        list.append(pickle.load(input))
                    except EOFError:
                        break
        except IOError:
            print 'No tickers on watch!'

    def add_ticker(self, ticker):
        stock = stock(ticker)
        if stocks is False:
            return False 
        with open('list_data.pkl', 'wb') as output:
            pickle.dump(stock, output, pickle.HIGHEST_PROTOCOL)
        print('Symbol: %s has been added to watchlist!' % ticker)

    def print_list(self):
        for stocks in list:
            print(stocks.get_ask_price()+ '\n')
