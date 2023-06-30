fruits = ['apple','banana','orange']
fruits.append('grape')
print(fruits)
fruits[0] = 'cherry'
print(fruits)

for fruit in fruits:
  print('好きな果物は' + fruit + 'です')