import json
from pprint import pprint


def book_info(book, categories):
    category_id = book["categoryId"]
    for id in range(len(category_id)):
        for cat_type in categories:
            if category_id[id] == cat_type["id"]:
                category_id[id] = cat_type["name"]
    data = {'author': book["author"], 'categoryName': book["categoryId"], 'cover': book["cover"], 'description': book["description"], 'id': book["id"], 'priceSales': book["priceSales"],'title': book["title"]} 
    # 'categoryId': [151128, 50919]
    return data
    
    # 여기에 코드를 작성합니다.



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    book_json = open(current_dir / 'data' / 'book.json', encoding="utf-8")
    book = json.load(book_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding="utf-8"
    )
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
