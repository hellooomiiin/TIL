from django.shortcuts import render

# Create your views here.
def index(request):
    
    menus = ['순대국밥', '김치볶음밥', '10층']

    context = {
        'menus' : menus,
    }

    return render(request, "books/index.html", context)

# 요청과 동시에 변수도 함께 전달
# [주의사항] 변수 이름 urls.py와 동일하게 작성
def detail(request, menu):
    context = {
        'menu' : menu
    }

    return render(request, "books/detail.html", context)