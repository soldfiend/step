from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForms
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, ListView


# Create your views here.

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/about_news.html'
    context_object_name = 'articles'


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/delete_news.html'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create_news.html'
    form_class = ArticlesForms


def home_news(request):
    news = Articles.objects.order_by('name')
    print(news)
    return render(request, 'news/home_news.html', {
        'news': news
    })


# def delete_news(request):
#     return render(request, 'news/delete_news.html')

class NewsListView(ListView):
    model = Articles
    queryset = Articles.objects.all()
    template_name = 'news/test_home.html'


class NewsCreateView(CreateView):
    model = Articles
    template_name = 'news/create_news.html'
    form_class = ArticlesForms


# def add_news(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("news")
#         else:
#             error = 'Неправильно заполненно поле'
#     form = ArticlesForms()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'news/create_news.html', data)
