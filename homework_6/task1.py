def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    any_city = moscow.intersection(kazan)
    moscow_goods = moscow - kazan
    kazan_goods = kazan - moscow
    total_different = moscow.union(kazan)

    print(f'Можно забрать в любом из двух городов: {any_city}')
    print(f'Eсть только в Москве: {moscow_goods}')
    print(f'Eсть только в Казани: {kazan_goods}')
    print(f'Всего разных товаров на обоих складах: {len(total_different)} шт.')


if __name__ == '__main__':
    main()
