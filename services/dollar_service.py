
import requests

def get_current_dollar_data():
    url = "https://co.dolarapi.com/v1/trm"
    
    try:
        response = requests.get(url, timeout=10)
        
        response.raise_for_status()
        
        data = response.json()

        return data
    
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
        

        
def get_dollar_price(data):
    return data["valor"]

def get_dollar_currency(data):
    return data["unidad"]

def get_dollar_name(data):
    return data["nombre"]

def get_dollar_update_date(data):
    return data["fechaActualizacion"]



if __name__ == "__main__":
    
    data = get_current_dollar_data()
    print(get_dollar_price(data))
    print(get_dollar_currency(data))
    print(get_dollar_update_date(data))
    print(get_dollar_name(data))






