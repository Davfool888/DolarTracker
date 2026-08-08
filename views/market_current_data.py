

def show_current_market_data(market_data):
    print("=====================================") 
    print(
    f"Valor dólar: "
    f"{market_data['valor']:,.2f} "
    f"{market_data['unidad']}"
         )
    print(f"Fecha: {market_data['fechaActualizacion']}")
    print(f"{market_data['nombre']}")
    print("=====================================") 
    