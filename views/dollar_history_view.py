def show_dollar_history(dollar_history):
   
    print()
    print("========================================")
    print("  HISTORIAL DEL DOLAR - ULTIMOS REGISTROS ")
    print("========================================")
    
    print(
        f"{'FECHA':<30}"
        f"{'VALOR':<18}"
        f"{'MONEDA':<15}"
        f"{'CAMBIO':<1}"
    )
    
    for i in range(0, len(dollar_history)):
        
        current_index = len(dollar_history) - i - 1
        
        date = dollar_history[current_index]["vigenciadesde"]
        price = float(dollar_history[current_index]["valor"])
        currency = dollar_history[current_index]["unidad"]
        
        if i == 0: 
            porcentaje_cambio = "-"
            
        else:
            
            previus_index = len(dollar_history) - i
            
            price_before = float(dollar_history[previus_index]["valor"])
            
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
            f"{date:<30}"
            f"{price:<18}"
            f"{currency:<15}"
            f"{porcentaje_cambio:<1}"
        )
        
    

