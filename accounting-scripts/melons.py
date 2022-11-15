melon_names = {
    1: 'Honeydew',
    2: 'Crenshaw',
    3: 'Crane',
    4: 'Casaba',
    5: 'Cantaloupe',
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}

melons = []

for i in range(1, len(melon_names) + 1):
    melon = {
        'name': melon_names[i],
        'price': melon_prices[i],
        'seedless': melon_seedlessness[i],
        'flesh_color': None,
        'rind_color': None,
        'average_weight': None
    }
    melons.append(melon)
