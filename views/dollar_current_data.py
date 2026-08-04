

def dollar_current_data_view(dollar_data):
    print("=====================================") 
    print(
    f"Valor dólar: "
    f"{dollar_data['valor']:,.2f} "
    f"{dollar_data['unidad']}"
         )
    print(f"Fecha: {dollar_data['fechaActualizacion']}")
    print(f"{dollar_data['nombre']}")
    print("=====================================") 
    