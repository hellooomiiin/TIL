import json

from pathlib import Path

current_dir = Path(__file__).resolve().parent

def new_books(books):
    list_book = list()
    # 여기에 코드를 작성합니다.
    for book in books:
        book_id = book["id"]
        book_num_json = open(current_dir / 'data' / 'books' / f'{book_id}.json', encoding='utf-8')
        book_num_detail = json.load(book_num_json)
        book_pub_date = book_num_detail["pubDate"]
        book_pub_year = book_pub_date[0:4]
        if book_pub_year == str(2023):
            list_book.append(book_num_detail["title"])
    return list_book


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    print(new_books(books))
