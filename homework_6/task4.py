from typing import TypedDict


class Day(TypedDict):
    day: str
    orders: int
    revenue: int
    returns: int


def main():
    days: list[Day] = [
        {"day": "пн", "orders": 20, "revenue": 40000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48000, "returns": 3},
    ]

    total_revenue = sum([day['revenue'] for day in days])
    best_day = max(days, key=lambda day: day['revenue'])['day']
    revenue_per_order = [day['revenue'] / day['orders'] for day in days]
    days_more_20_returns = [day['day']
                            for day in days
                            if day['returns'] / day['orders'] > 0.2]

    print(f'Выручка за всю неделю: {total_revenue}')
    print(f'День с самой большой выручкой: {best_day}')
    print(f'Среднее на один заказ по дням: {revenue_per_order}')
    print(f'Дни с более 20% возвратов: {days_more_20_returns}')


if __name__ == '__main__':
    main()
