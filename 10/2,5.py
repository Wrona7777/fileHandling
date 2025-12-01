import os
os.chdir(os.path.dirname(__file__))

shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
   with open(file_name,'a') as cart:
      cart.write(f"{product_name}\n")

# Takes next product name from the keyboard
product = ""
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      break
   else:
      add_product(shopping_list,product)