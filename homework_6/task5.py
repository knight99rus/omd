from itertools import groupby
from typing import TypedDict


class Review(TypedDict):
    id: int
    product: str
    stars: int


class ProductStats(TypedDict):
    avg: float
    count: int


reviews: list[Review] = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

reviews = [{'id': review['id'],
            'product': review['product'].lower(),
            'stars': review['stars']} for review in reviews]
reviews.sort(key=lambda review: review['id'])

stats: dict[str, ProductStats] = {}
for _, group_iter in groupby(reviews, key=lambda review: review['id']):
    group = list(group_iter)
    stars = [review['stars'] for review in group]
    stats[group[0]['product']] = {
        'avg': sum(stars) / len(stars),
        'count': len(stars),
    }

averages = [{product: s['avg']} for product, s in stats.items()]
candidates = {product: s for product, s in stats.items() if s['count'] >= 2}
worst = min(candidates, key=lambda product: candidates[product]['avg'])
low_count = sum(1 for review in reviews if review['stars'] <= 2)
share = low_count / len(reviews)

print(f'Средние оценки: {averages}')
print(f'Худший товар: {worst}')
print(f'Отзывов на 1 или 2 звезды: {low_count}')
print(f'Доля от всех отзывов: {share:.0%}')
