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
    
    return category_option







        
while is_running: 
    try:
        category_option = show_category_operation()
        
        if category_option == 1:
            run_dollar_market()
             
        elif category_option == 2: 
            print(
                "El mercado de acciones "
                "estará disponible "
                "próximamente."
            )
        elif category_option == 3: 
                    print(
                        "El mercado de criptomonedas"
                        "estará disponible "
                        "próximamente."
                    )
                    
        elif category_option == 4: 
            print("Programa finalizado")
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



