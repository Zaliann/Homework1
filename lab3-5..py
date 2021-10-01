surname = input('Введите фамилию')
name = input('Введите имя')
group = input('Введите группу')
print('Привет,' + surname + ' ' + name + 'из группы ' + group + '!')
mail = input('Введи свою электронную почту?')
l = surname[0:5] + 2 * name[0:5] + 3 * mail[0:5]
print(l.lower())
