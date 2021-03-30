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
        print('\t' + topping)

# find the name with domain
email_list = {
    'gmail.com': ['abir.yusuf', 'mim.montaha', 'clark.kent'],
    'yahoo.com': ['barbara.gordon', 'jean.grey'],
    'hotmail.com': ['bruce.wayne']
}
for domain, emails in email_list.items():
    print('\n' + domain.title() + ' is related with:')
    for email in emails:
        print(email.title())

# for gmail, name in email_list:
#     email = []
#     for names in name:
#         email.append(names + '@' + gmail)
#         print(email)
#
#     print("\t" + gmail)

# A dictionary in a dictionary
# A dictionary in a dictionary
user = {
    'abiryusuf': {
        'first': 'abir',
        'last': 'yusuf',
        'location': 'NY'

    },
    'mimmontaha': {
        'first': 'mim',
        'last': 'madiha',
        'location': 'Bangladesh'
    },
}

for username, user_info in user.items():
    for usernames in username:
        print('\nUsername: ' + username)
        fullName = user_info['first'] + ' ' + user_info['last']
        location = user_info['location']
        print('\tFull name: ' + fullName.title())
        print('\tLocation: ' + location.title())
