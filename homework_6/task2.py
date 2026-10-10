from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

total = len(queries)
total_by_query = Counter(queries)
top_popular = total_by_query.most_common(1)[0][0]
top_frequent = total_by_query.most_common(1)[0][1]
most_frequent_share = float(top_frequent) / total
one_queries = [k for k, v in total_by_query.items() if v == 1]

print(f'Всего поисковых запросов: {total}')
print(f'Статистика по введенным запросам: {total_by_query}')
print(f'Самый частый запрос: {top_popular}')
print(f'Он занимает {most_frequent_share:.3f}% от всех поисков')
print(f'Один раз встретились следующие запросы: {one_queries}')
