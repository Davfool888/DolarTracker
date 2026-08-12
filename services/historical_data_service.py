import json 
from models.market_candle import MarketCandle

def get_historical_sample(limit=10):
    file_path = "data/raw/xbtusd_1m.json"
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        
    candles = []
    
    for row in data[:limit]: 
        
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
    
    if candle.low_price < candle.open_price:
        return False
        
    if candle.low_price < candle.close_price:
        return False
        
    if candle.volumen < 0:
        return False
    
    return True

if __name__ == "__main__":

    candles = get_historical_sample(10)
    for candle in candles:
        
        is_valid = validate_candle(candle)
        
        print(
            candle.timestamp, "VALIDA" if is_valid else "INVALIDAD"
        )


