from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
#   - 게시글 작성  ( /create/ )
    path('create/', views.create, name='create'),
#   - 게시글 전체 조회  ( / )
    path('', views.index, name='index'),
#   - 게시글 상세 조회  ( /<int:id>/ )
    path('<int:id>', views.detail, name='detail')
#   - 게시글 수정  ( /<int:id>/update/ )
#   - 게시글 삭제  ( /<int:id>/delete/ )
]
