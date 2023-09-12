from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_news, name='news'),
    path('add_news', views.NewsCreateView.as_view(), name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update')

]
