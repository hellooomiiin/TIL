# 아래 함수를 수정하시오.
def check_number():
    try:
        num = int(input("숫자를 입력하세요 : "))
        if num > 0:
            print("양수입니다.")
        elif num == 0:
            print("0입니다.")
        else:
            print("음수입니다.")
    except ValueError:
        print("잘못된 입력입니다.")

check_number()

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        name = input("이름을 입력하세요: ")
        age = input("나이를 입력하세요: ")
        try:
            age = int(age)
            self.user_data["이름"] = name
            self.user_data["나이"] = age
        except ValueError:
            print("나이는 숫자로 입력해야 합니다.")
        

    def display_user_info(self):
        if not self.user_data:
            print("사용자 정보가 입력되지 않았습니다.")
        else:
            print("사용자 정보: ")
            print(f"이름 : {self.user_data['이름']}")
            print(f"나이 : {self.user_data['나이']}")

user = UserInfo() # 인스턴스 생성
user.get_user_info()
user.display_user_info()
