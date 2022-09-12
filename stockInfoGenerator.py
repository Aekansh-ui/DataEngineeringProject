from ast import main
import yfinance as yf

class stock_data:
    
    def __init__(self,stock_name="^NSEI") -> None:
        self.stock_name = stock_name
    
    def get_data(self):
        data = yf.Ticker(self.stock_name)
        return data

if __name__ == '__main__':
    d = stock_data("DIXON.NS")
    print(d.get_data().info)
