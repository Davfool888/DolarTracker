def request_number(message, zero_value=True):
    while True:
        try:
            value = float(input(message))
            if zero_value:
                if value > 0:
                    return value
                else:
                    print("Valor tiene que ser mayor a 0")
            else:
                if value < 0:
                    print("Valor no puede ser negativo")
                else:
                    return value
                    

            return value
            
        except ValueError:
            print("El valor debe ser un número. Intenta nuevamente.")