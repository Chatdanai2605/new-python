phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-4444'}
heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Ironman'] = '888-2222'
print(heroesdict.get('Halk', 'Key Not Found'))
print(heroesdict.get('Hulk', 'Key Not Found'))

for key,value in heroesdict.items():
    print(key, value)


print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mick', 'Element Not Found'))
print(phonebook.pop('Mickey', 'Element Not Found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)