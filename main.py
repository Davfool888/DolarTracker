from utils.input_utils import  request_integer
from controllers.dollar_controller import run_dollar_market



is_running = True 





def show_category_operation():
    print("""
=====================================
              MARKET
=====================================

Seleccione el mercado:

1. Dólar USD/COP
2. Acciones
3. Criptomonedas
4. Salir
          """)
    
    category_option = request_integer("Elige una opcion: ")
    
    if category_option == 1: 
        return "USD/COP"
    elif category_option == 2: 
        return "STOCK"
    elif category_option == 3: 
        return "CRYPTO" 
    elif category_option == 4: 
        return "EXIT"
    else:
        print("Opción inválida. "
            "Intenta nuevamente.")
        
        return None







        
while is_running: 
    try:
        select_market = show_category_operation()
        
        if select_market == "USD/COP":
            run_dollar_market(select_market)
            
        elif select_market == "CRYPTO":
            print(
        "El mercado de Cripto "
        "estará disponible "
        "próximamente."
                 )
            
        elif select_market == "STOCK":
                    print(
                "El mercado de Acciones "
                "estará disponible "
                "próximamente."
                         )
                    
        elif select_market == "EXIT":
                     print(
        "Programa finalizado.")
                     is_running = False
                     
        elif select_market == None: 
            continue

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



