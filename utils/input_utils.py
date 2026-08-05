def request_number(message, allow_zero=False):

    while True:

        try:
            value = float(input(message))

            if allow_zero:
                if value >= 0:
                    return value
                print("El valor no puede ser negativo.")

            else:
                if value > 0:
                    return value

                print("El valor debe ser mayor a 0.")

        except ValueError:

            print(
                "El valor debe ser un número. "
                "Intenta nuevamente."
            )

def request_integer(messege, zero_allow=False):
    while True:
        try:
            value = int(input(messege)) 
            
            if zero_allow:
                if value >= 0:
                    return value
                print("El valor debe ser mayor o igual a 0")
            else:
                if value > 0: 
                    return value    
                print("El valor debe ser mayor a 0")    
        except ValueError:
            print( "El valor debe ser un número. "
                            "Intenta nuevamente.")