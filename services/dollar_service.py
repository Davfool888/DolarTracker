
import requests
from models.market_data import MarketData

def get_current_dollar_data():
    url = "https://co.dolarapi.com/v1/trm"
    
    try:
        response = requests.get(url, timeout=10)
        
        response.raise_for_status()
        
        data = response.json()
        
        market_data = MarketData(
            market="USD/COP",
            price= float(data["valor"]),
            currency=data["unidad"],
            updated_at=data["fechaActualizacion"]
            
        )

        return market_data
    
    except requests.exceptions.Timeout:
        raise ConnectionError("La consulta del dólar tardó demasiado. "
            "Intenta nuevamente.")
        
    except requests.exceptions.ConnectionError:
        raise ConnectionError("No fue posible conectarse con "
            "el servicio del dólar.")
        
    except requests.exceptions.HTTPError:
        raise ConnectionError("El servicio del dólar respondió "
            "con un error.")
        
    except requests.exceptions.RequestException:
        raise ConnectionError("Ocurrió un error al consultar "
            "el precio del dólar.")
        





if __name__ == "__main__":
    
    data = get_current_dollar_data()
    
    print(data.currency)





