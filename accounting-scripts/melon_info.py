"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melon):
    """Print each melon with corresponding attribute information."""

    print(
    f'''{melon['name'].upper()}
price: {melon['price']}
seedless: {melon['seedless']}
flesh_color: {melon['flesh_color']}
rind_color: {melon['rind_color']}
average_weight: {melon['average_weight']}
    ''')


for melon in melons:
    print_melon(melon)
