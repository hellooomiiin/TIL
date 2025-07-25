import json

from pathlib import Path

current_dir = Path(__file__).resolve().parent

def best_book(books):
    max_rank = 0
    # 여기에 코드를 작성합니다.
    for book in books:
        book_id = book["id"]
        book_num_json = open(current_dir / 'data' / 'books' / f'{book_id}.json', encoding='utf-8')
        book_num_detail = json.load(book_num_json)
        book_rank = book_num_detail["customerReviewRank"]
        if max_rank < book_rank:
            max_rank = book_rank
            max_book = book_num_detail["title"]


    return max_book


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    print(best_book(books))

    


# # 반복문을 통해 books 폴더 내부의 파일들을 열기

# # open 및 json 모듈 사용예시

# # JSON 형식의 파일을 처리하기 위한 내장 모듈
# import json

# # 파일 시스템 경로를 객체 지향적으로 다루기 위한 모듈
# from pathlib import Path


# # 현재 실행 중인 파일의 절대 경로를 기준으로 부모 디렉토리 경로 설정
# # - Path(__file__): 현재 파일의 경로를 Path 객체로 변환
# # - resolve(): 실제 경로로 변환하고 절대 경로를 반환
# # - parent: 부모 디렉토리 경로를 반환
# current_dir = Path(__file__).resolve().parent


# # 파일 열기
# # open('파일경로', encoding='인코딩방식')
# # - current_dir / 'sample.json': Path 객체의 / 연산자로 경로 결합
# # - encoding="utf-8"은 한글 등 유니코드 문자를 올바르게 처리하기 위한 설정
# book = open(current_dir / 'sample.json', encoding='utf-8')

# # json.load()로 JSON 파일의 내용을 파이썬 데이터로 변환
# # - JSON의 object → 파이썬 딕셔너리
# # - JSON의 array → 파이썬 리스트
# # - JSON의 string → 파이썬 문자열
# # - JSON의 number → 파이썬 정수/실수
# book_detail = json.load(book)

# # 변환된 파이썬 데이터 출력
# print(book_detail)