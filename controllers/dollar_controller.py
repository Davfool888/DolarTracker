from models.investment import Investment
from views.investment_view import show_investment_summary
from views.market_current_data import show_current_market_data
from views.market_history_view import show_market_history
from utils.input_utils import request_integer, request_number
from services.dollar_service import get_dollar_price
from services.market_service import get_current_market_data, get_market_history


def request_investment_data(select_market):
    data = get_current_market_data(select_market)
    
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
               USD/COP
=====================================

1. Analizar una inversión
2. Mostrar precio dolar
3. Mostrar historial de los últimos 15 días
4. Salir
""")
    menu_option= request_integer("Elige una opcion: ")

    return menu_option



def select_registers():
    registers = request_integer("Elige el número de días "
            "a ver en el historial: ")
    return registers


def run_dollar_market(selected_market):
    is_dollar_market_running = True
    
    while is_dollar_market_running:
        option = show_menu()
        
        if option == 1:
            investment = request_investment_data(selected_market)
            show_investment_summary(investment)
                        
        elif option == 2:
            market_data = get_current_market_data(selected_market) 
            show_current_market_data(market_data)
                        
        elif option == 3:
            registers = select_registers()
            market_history = get_market_history(selected_market, registers)
            show_market_history(market_history)
                
        elif option == 4: 
            print("Saliendo del mercado "
                "USD/COP.")
            is_dollar_market_running = False
        else:
            print("Opción inválida. Intenta nuevamente.")