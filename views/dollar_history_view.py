def show_dollar_history(dollar_history):
    print()
    print("========================================")
    print("  HISTORIAL DEL DOLAR - ULTIMOS 15 DIAS ")
    print("========================================")
    
    print(
        f"{'FECHA':<20}"
        f"{'VALOR':>18}"
        f"{'MONEDA':>10}"
    )
    
    for day in dollar_history:
        
        date = day["vigenciadesde"]
        price = float(day["valor"])
        currency = day["unidad"]
        
        print(
            f"{date:<20}"
            f"{price:>18}"
            f"{currency:>19}"
        )
        
    

