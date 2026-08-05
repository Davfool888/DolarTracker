import requests

def get_dollar_history(days):
    
    try: 
        url = f"https://www.datos.gov.co/resource/mcec-87by.json?$order=vigenciadesde DESC&$limit={days}"
        response = requests.get(url, timeout =10)
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
        
if __name__ == "__main__":
    print(get_dollar_history())