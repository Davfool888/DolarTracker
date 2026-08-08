def show_market_history(market_history):
   
    print()
    print("========================================")
    print("  HISTORIAL DEL DOLAR - ULTIMOS REGISTROS ")
    print("========================================")
    
    print(
        f"{'ID':<26}"
        f"{'FECHA':<25}"
        f"{'VALOR':<18}"
        f"{'MONEDA':<15}"
        f"{'CAMBIO':<1}"
    )
    
    for i in range(0, len(market_history)):
        
        current_index = len(market_history) - i - 1
        id_register = i
        date = market_history[current_index]["vigenciadesde"]
        price = float(market_history[current_index]["valor"])
        currency = market_history[current_index]["unidad"]
        
        if i == 0: 
            porcentaje_cambio = "-"
            
        else:
            
            previus_index = len(market_history) - i
            
            price_before = float(market_history[previus_index]["valor"])
            
            cambio = ((price - price_before) / price_before) * 100
            
            if cambio > 0:
                porcentaje_cambio = f"↑ {cambio:.2f}%"
            elif cambio < 0:
                porcentaje_cambio = f"↓ {cambio:.2f}%"
            else:
                porcentaje_cambio = (
                    "→ 0.00%"
                )
                
                
                
    
       
        
        print(
            f"{id_register:<26}"
            f"{date:<25}"
            f"{price:<18}"
            f"{currency:<15}"
            f"{porcentaje_cambio:<1}"
        )
        
    

