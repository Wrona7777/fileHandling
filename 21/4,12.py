import csv

def get_output_filename(genre):
    mapping = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }
    return mapping.get(genre.strip())

def process_books():
    with open('books.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = get_output_filename(row['Genre'])
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"{row['Title']},{row['Author']},{row['Year']}\n")

process_books()