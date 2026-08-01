class Investment: 

    def __init__(self, capital_cop, purchase_price, sale_price, total_costs, target_profit):

        if capital_cop <= 0: 
                    raise ValueError("Capital_cop debe ser mayor a 0")
        if purchase_price <= 0: 
                    raise ValueError("Precio de compra debe ser mayor a 0")
        if sale_price <= 0: 
                    raise ValueError("sale_price debe ser mayor a 0")
        if total_costs < 0: 
                    raise ValueError("Costos deben debe ser mayor o igual a 0")
        if target_profit <= 0: 
                    raise ValueError("Ganancia Objetivo debe ser mayor a 0")
        
        self.capital_cop = capital_cop
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.total_costs = total_costs
        self.target_profit = target_profit


    def calculate_dollars_purchased(self):
        return self.capital_cop / self.purchase_price
         
    def calculate_gross_profit(self):
        return self.calculate_dollars_purchased() * self.sale_price - self.capital_cop

    def calculate_net_profit(self):
        return self.calculate_gross_profit() - self.total_costs

    def has_reached_target(self):
        return self.calculate_net_profit() >= self.target_profit

    def calculate_minimum_sale_price(self):
        return (self.capital_cop + self.total_costs + self.target_profit) / self.calculate_dollars_purchased()

    def show_summary(self):
        print("=====================================")

        print(f"Capital invertido:")
        print(f"${self.capital_cop:,} COP")
        print()

        print("Precio de compra:")
        print(f"${self.purchase_price:,} COP/USD")
        print()

        print("Dolares adquiridos:")
        print(f"${self.calculate_dollars_purchased():.2f} USD")
        print()

        print("Ganancia Bruta:")
        print(f"${self.calculate_gross_profit():,} COP")
        print()

        print("Costos:")
        print(f"${self.total_costs:,} COP")
        print()

        print("Ganancia neta:")
        print(f"${self.calculate_net_profit():,} COP")
        print()

        print("Ganancia Objetivo:")
        print(f"${self.target_profit:,} COP")
        print()

        print("Precio minimo de venta:")
        print(f"${self.calculate_minimum_sale_price():,} COP/USD")
        print()

        print("Estado:")
        if self.has_reached_target():
            print("OBJETIVO ALCANZADO")
        else:
            print("OBJETIVO NO ALCANZADO")  

        print("=====================================")  


