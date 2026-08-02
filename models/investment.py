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


       

