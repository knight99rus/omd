from collections import Counter
from typing import TypedDict


class Order(TypedDict):
    id: int
    buyer: str
    status: str
    amount: int


orders: list[Order] = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2100},
]

total_returns = sum([order['amount']
                     for order in orders
                     if order['status'] == 'returned'])
returned_customers = set([order['buyer']
                          for order in orders
                          if order['status'] == 'returned'])
total_delivered = Counter([order['buyer']
                           for order in orders
                           if order['status'] == 'delivered'])
delivered_orders = [order['amount']
                    for order in orders
                    if order['status'] == 'delivered']
average_amount = sum(delivered_orders) / len(delivered_orders)

print(f'Оформлено возвратов на сумму {total_returns}')
print(f'Хоть раз вернули заказ: {returned_customers}')
print(f'Статистика доставок покупателям: {total_delivered}')
print(f'Средний чек: {average_amount}')
