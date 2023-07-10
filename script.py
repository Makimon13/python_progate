# 02/07/23
# lesson 7 
# for loop
#  fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

#  for makito in fruits:
#      print(makito + 'は' + fruits[makito] + 'という意味です')

# lesson 8 while
# x = 10

# while x > 0:
#     print(x)
#     x -= 1


# 04/07/23
# numbers = [765, 921, 777, 256]
# for number in numbers:
#     print(number)
#     if number == 777:
#       print('777が見つかったので処理を終了します')
#       break

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     # 変数 number の値が 3 の倍数のとき、繰り返し処理をスキップしてください
#     if number % 3 == 0:
#       continue
    
#     print(number)

# 08/07/23
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money = money - total_price

        if money == 0:
          print('財布が空になりました')
          break
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
print('残金は' + str(money) + '円です')
