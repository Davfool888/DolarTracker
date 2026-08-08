class MarketData: 
    def __init__(self, market, price, currency, updated_at):
        self.market = market
        self.price = price
        self.currency = currency
        self.updated_at = updated_at
        
    def show_info(self):
        return {
            self.market,
            self.price,
            self.currency,
            self.updated_at
            
        }
    
    
if __name__ == "__main__":
    
    market_data = MarketData(
        market="USD/COP",
        price=4300.50,
        currency="COP",
        updated_at="2026-08-05"
    )
    
print(market_data.show_info())