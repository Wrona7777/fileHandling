import csv

with open('clothing.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row['Price'])
        stock = int(row['Stock_Quantity'])
        if price < 60 and stock < 40:
            print(f"{row['Product_Name']} ({row['Size']}, {row['Color']}) - {price} - {stock} szt.")