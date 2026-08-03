from models.investment import Investment
from views.investment_view import show_investment_summary
from utils.input_utils import request_number

is_running = True 

def request_investment_data():
    capital_cop = request_number("Ingrese el capital en COP: ")
    purchase_price = request_number("Ingrese el precio de compra: ")
    sale_price= request_number("Ingrese el precio de venta: ")
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
2. Salir
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



