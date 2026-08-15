import json 
from models.market_candle import MarketCandle
from models.market_segment import MarketSegment

def get_historical_sample(limit=10):
    file_path = "data/raw/xbtusd_1m.json"
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    data = sorted(data, key=lambda row: row[0])
        
    candles = []
    
    for row in data[:limit]: 
        
        print(row)
        
        candle = MarketCandle(
            timestamp=row[0],
            market="BTC/USD",
            timeframe="1m",
            open_price=float(row[1]),
            high_price=float(row[2]),
            low_price=float(row[3]),
            close_price=float(row[4]),
            volumen=float(row[5])    
        )
        
        candles.append(candle)
    
    return candles

def validate_candle(candle):
    
    if candle.high_price < candle.open_price:
        return False
    
    if candle.high_price < candle.close_price:
        return False
    
    if candle.high_price < candle.low_price:
        return False
    
    if candle.low_price > candle.open_price:
        return False
        
    if candle.low_price > candle.close_price:
        return False
        
    if candle.volumen < 0:
        return False
    
    return True
def segment_candles(candles):
    segments = []
    current_segment = []
    
    for i, candle in enumerate(candles):
        if i == 0:
            current_segment.append(candle)
            continue
        previous = candles[i -1]
        
        difference = (candle.timestamp - previous.timestamp)
        
        minutes = difference.total_seconds() / 60
        
        if minutes == 1:
            current_segment.append(candle)
        else:
            segments.append(current_segment)
            current_segment = [candle]
    if current_segment:
        segments.append(current_segment)
    return segments


        
if __name__ == "__main__":

    candles = get_historical_sample(20)
    segment = MarketSegment(candles=candles, timeframe="1m")
    print("Inicio:", segment.start)
    print("Fin:", segment.end)
    print("Timeframe:", segment.timeframe)
    print("Cantidad:", len(segment.candles))
    print("Continuous:", segment.is_continuous())