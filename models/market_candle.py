class MarketCandle:
    def __init__(self, timestamp, market, timeframe, open_price, high_price, low_price, close_price, volumen):
        self.timestamp = timestamp
        self.market = market
        self.timeframe = timeframe
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volumen = volumen
        
        