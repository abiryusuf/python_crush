aliens = []
for alien in range(30):
    new_aliens = {'color': 'green', 'point': 4, 'speed:': 'slow'}
    aliens.append(new_aliens)

for alien in aliens[:5]:
    print(alien)

# A list in dictionary
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra chess', 'chicken']
}
print("I ordered a " + pizza['crust'] + '- crust pizza')
