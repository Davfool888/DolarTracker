class Investment: 

    def __init__(self, capital_cop, purchase_price, sale_price, total_costs, target_profit):
        self.capital_cop = capital_cop
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.total_cost = total_costs
        self.target_profit = target_profit


    def calculate_dollars_purchased(self):
        return self.capital_cop / self.purchase_price


    def calculate_gross_profit(self):
        return self.calculate_dollars_purchased() * self.sale_price - self.capital_cop

    def calculate_net_profit(self):
        return self.calculate_gross_profit() - self.total_cost


investment = Investment(
    capital_cop=1_000_000,
    purchase_price=4_000,
    sale_price=4_180,
    total_costs=10_000,
    target_profit=30_000
)


print(investment.calculate_dollars_purchased())
print(investment.calculate_gross_profit())
print(investment.calculate_net_profit())