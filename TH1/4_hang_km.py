def is_purchase_possible(prices, notifications, budget):
    total_store_cost = 0

    for i in range(len(prices)):
        if "lower than in-store" in notifications[i]:
            percent_index = notifications[i].find('%')
            discount = float(notifications[i][percent_index - 3:percent_index]) / 100
            total_store_cost += prices[i] * (1 - discount)
        elif "higher than in-store" in notifications[i]:
            percent_index = notifications[i].find('%')
            extra_price = float(notifications[i][percent_index - 3:percent_index]) / 100
            total_store_cost += prices[i] * (1 + extra_price)
        else:
            total_store_cost += prices[i]

    return total_store_cost <= budget

item_prices = list(map(int, input().split()))
item_notifications = [input().strip() for _ in range(len(item_prices))]
available_budget = int(input().strip())

if is_purchase_possible(item_prices, item_notifications, available_budget):
    print("true")
else:
    print("false")
