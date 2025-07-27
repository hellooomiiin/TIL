import json
from pprint import pprint


def books_info(books, categories):
    # 여기에 코드를 작성합니다.
    book_data = list()
    for book in books:
        category_id = book["categoryId"]
        for id in range(len(category_id)):
            for cat_type in categories:
                if category_id[id] == cat_type["id"]:
                    category_id[id] = cat_type["name"]
                    
        data = {'author': book["author"], 
                'categoryName': book["categoryId"], 
                'cover': book["cover"], 
                'description': book["description"], 
                'id': book["id"], 
                'priceSales': book["priceSales"],
                'title': book["title"]}
        book_data.append(data)
    return book_data
    # 'categoryId': [151128, 50919]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding='utf-8'
    )
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
