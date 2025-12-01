with open('powers.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 101):
        line = f"{i},{i**2},{i**3}"
        print(line)
        f.write(line + '\n')