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

for topping in pizza['topping']:
    if topping == 'mushrooms':
        print('\t' + topping)

# find the name with domain
email_list = {
    'gmail.com': ['abir.yusuf', 'mim.montaha', 'clark.kent'],
    'yahoo.com': ['barbara.gordon', 'jean.grey'],
    'hotmail.com': ['bruce.wayne']
}

for gmail, name in email_list:
    email = []
    for names in name:
        email.append(names + '@' + gmail)
        print(email)

    print("\t" + gmail)
