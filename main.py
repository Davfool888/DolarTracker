from models.investment import Investment

investment = Investment(
    capital_cop=1_000_000,
    purchase_price=4_000,
    sale_price=4_180,
    total_costs=10_000,
    target_profit=30_000
)

investment.show_summary()