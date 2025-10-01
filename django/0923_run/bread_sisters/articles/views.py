from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    response = render(request, 'articles/index.html', context)
    response.set_cookie(
        key='username',
        value='giryun',
    )
    return response

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
        
        
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    
    context = {
        'article' : article,
    }
    
    return render(request, 'articles/detail.html', context)