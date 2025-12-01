with open("it_company.csv") as plik:
    content = plik.read().splitlines()

i = 0
for line in content:
        print(line)
        i+=1
        if i == 5:
            while True:
                    user = input("Press enter... ")
                    if user == "":
                         i=0
                         break