import csv

with open('it_company.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    designers = []
    for row in csv_reader:
        if row.get('Job Title', '').strip() == 'Graphic Designer':
            first_name = row.get('First Name', '').strip()
            last_name = row.get('Last Name', '').strip()
            email = row.get('Email', '').strip()
            full_name = f"{first_name} {last_name}"
            designers.append(f"{full_name},{email}")
    
    print("GRAPHIC DESIGNERS")
    print("=================")
    if designers:
        for designer in designers:
            print(designer)
    else:
        print("Brak grafik designerów w pliku.")