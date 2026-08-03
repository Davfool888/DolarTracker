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