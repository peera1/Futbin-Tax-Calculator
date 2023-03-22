def calculate_initial_price_for_given_sale_price(sale_price, desired_profit, tax_rate):
    initial_price = sale_price / (1 + tax_rate) - (desired_profit / (1 + tax_rate))
    return initial_price



sale_price = 4000
desired_profit = 100
tax_rate = 0.05

initial_price = calculate_initial_price_for_given_sale_price(sale_price, desired_profit, tax_rate)
print(f"To achieve a net profit of ${desired_profit:.2f} after selling the stock at the current market price of ${sale_price:.2f} with a {tax_rate*100:.0f}% tax rate, you should initially purchase the stock at around ${initial_price:.2f}.")
