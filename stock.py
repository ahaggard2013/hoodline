from Robinhood import Robinhood

#########################################################
##Holds information about stocks you would like to save##
#########################################################

class stock:
    ticker = None
    current_ask_price = None
    prev_close = None

    def __init__(self, ticker):
        robinhood = Robinhood()
        self.ticker = ticker
        try:
            self.current_ask_price = float(str(robinhood.ask_price(ticker)))
            self.prev_close = float(str(robinhood.previous_close(ticker)))
        except NameError:
            print ('Invalid Symbol: %s' % ticker)
            return False

    def get_ask_price(self):
        return self.current_ask_price

    def get_prev_close(self):
        return self.prev_close
