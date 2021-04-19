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

def skip_elements_two(elements):
    ele = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            ele.append("{}".format(element))
    return ele

print(skip_elements_two("a", "b", "c", "d"))
