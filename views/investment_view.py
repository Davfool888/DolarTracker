

def show_investment_summary(investment):
            print("=====================================")
    
            print(f"Capital invertido:")
            print(f"${investment.capital_cop:,.2f} COP")
            print()
    
            print("Precio de compra:")
            print(f"${investment.purchase_price:,.2f} COP/USD")
            print()
    
            print("Dolares adquiridos:")
            print(f"${investment.calculate_dollars_purchased():.2f} USD")
            print()
    
            print("Ganancia Bruta:")
            print(f"${investment.calculate_gross_profit():,.2f} COP")
            print()
    
            print("Costos:")
            print(f"${investment.total_costs:,.2f} COP")
            print()
    
            print("Ganancia neta:")
            print(f"${investment.calculate_net_profit():,.2f} COP")
            print()
    
            print("Ganancia Objetivo:")
            print(f"${investment.target_profit:,.2f} COP")
            print()
    
            print("Precio minimo de venta:")
            print(f"${investment.calculate_minimum_sale_price():,.2f} COP/USD")
            print()
    
            print("Estado:")
            if investment.has_reached_target():
                print("OBJETIVO ALCANZADO")
            else:
                print("OBJETIVO NO ALCANZADO")  
    
            print("=====================================")  
    