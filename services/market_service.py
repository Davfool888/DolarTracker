from services.dollar_service import get_current_dollar_data
from services.dollar_history_service import get_dollar_history

def get_current_market_data(market):
    
    if market == "USD/COP":
        return get_current_dollar_data()
    raise ValueError("El mercado seleccionado "
        "no está disponible.")
    
def get_market_history(market, registers):  
    
        if market == "USD/COP":
            return get_dollar_history(registers)
        raise ValueError("El historial del mercado "
        "seleccionado no está disponible.")
    
if __name__ == "__main__":
    market_data = get_current_market_data("USD/COP")
    print(market_data)
    
    

            
        
    