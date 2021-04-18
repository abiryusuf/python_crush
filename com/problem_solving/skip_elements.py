def skip_elements(elements):
    new_items = []
    i = 0
    for x in elements:
        if i % 2 == 0:
            new_items.append(x)
            # or
            # new_items = new_items + [x]
        i += 1
    return new_items

print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))