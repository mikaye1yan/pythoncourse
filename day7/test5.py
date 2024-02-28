info1 = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}
info2 = {
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
}
info3 = {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}
total_profit1 = round((info1["sell_price"] - info1["cost_price"]) * info1["inventory"])
total_profit2 = round((info2["sell_price"] - info2["cost_price"]) * info2["inventory"])
total_profit3 = round((info3["sell_price"] - info3["cost_price"]) * info3["inventory"])
print(total_profit1)  
print(total_profit2)  
print(total_profit3)  