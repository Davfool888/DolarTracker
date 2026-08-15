class MarketSegment: 
    def __init__(self, candles, timeframe):
        self.candles = candles
        self.timeframe = timeframe
        
        self.start = candles[0].timestamp
        self.end = candles[-1].timestamp
        
        
    def is_continuous(self):
        for i in range(1, len(self.candles)):
            previus = self.candles[i -1]
            current = self.candles[i]
            
            difference = current.timestamp - previus.timestamp 
            minutes = difference.total_seconds() / 60 
            
            if minutes != 1:
                return False
        return True