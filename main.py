from models.investment import Investment
from views.investment_view import show_investment_summary
from utils.input_utils import request_number

is_running = True 



        
while is_running: 
    try: 
        capital_cop = request_number("Ingrese el capital en COP: ")
        purchase_price = request_number("Ingrese el precio de compra: ")
        sale_price= request_number("Ingrese el precio de venta: ")
        total_costs= request_number("Ingrese los costos totales: ", zero_value=False)
        target_profit= request_number("Ingrese la ganancia objetivo: ")

        investment = Investment(

        capital_cop= capital_cop,
        purchase_price= purchase_price,
        sale_price=sale_price,
        total_costs=total_costs,
        target_profit=target_profit
        )
    
        show_investment_summary(investment)

        is_running = False

    except ValueError as error:
        print()
        print("=====================================") 
        print("No se pudo realizar la conversion")
        print(error)
        print("=====================================") 
        print()
    except Exception as error:
        print()
        print("=====================================") 
        print("No se pudo realizar la conversion")
        print(error)
        print("=====================================") 
        print()



