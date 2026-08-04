from models.investment import Investment
from views.investment_view import show_investment_summary
from views.dollar_current_data import dollar_current_data_view
from views.dollar_history_view import show_dollar_history
from utils.input_utils import request_number
from services.dollar_service import get_current_dollar_data, get_dollar_price
from services.dollar_history_service import get_dollar_history

is_running = True 

def request_investment_data():
    data = get_current_dollar_data()
    
    capital_cop = request_number("Ingrese el capital en COP: ")
    purchase_price = request_number("Ingrese el precio de compra ")
    sale_price= get_dollar_price(data)
    print(f"Precio de venta es {sale_price:,.2f}")
    total_costs= request_number("Ingrese los costos totales: ", allow_zero=True)
    target_profit= request_number("Ingrese la ganancia objetivo: ")

    investment = Investment(

    capital_cop= capital_cop,
    purchase_price= purchase_price,
    sale_price=sale_price,
    total_costs=total_costs,
    target_profit=target_profit
    )

    return investment

def show_menu():

    print("""
=====================================
               IADOLAR
=====================================

1. Analizar una inversión
2. Mostrar precio dolar
3. Mostrar historial de los últimos 15 días
4. Salir
""")
    menu_option= int(input("Elige una opcion: "))

    return menu_option

        
while is_running: 
    try: 
        option = show_menu()
        if option == 1:
            investment = request_investment_data()
            show_investment_summary(investment)
            
        elif option == 2:
            dollar_data = get_current_dollar_data()
            dollar_current_data_view(dollar_data)
            
        elif option == 3:
            dollar_history = get_dollar_history()
            show_dollar_history(dollar_history)
    
        elif option == 4: 
            print("Programa finalizado.")
            is_running = False
        else:
            print("Opción inválida. Intenta nuevamente.")

    except ValueError as error:
        print()
        print("=====================================") 
        print("No se pudo realizar la operacion")
        print(f"Error, {error}")
        print("=====================================") 
        print()
    except Exception as error:
        print()
        print("=====================================") 
        print("No se pudo realizar la conversion")
        print(error)
        print("=====================================") 
        print()



