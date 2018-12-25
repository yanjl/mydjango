from django.urls import path
from django.views.generic import TemplateView

from .views import (IndexTemplate, ProductDetail, ProductList,
                    PublisherBookList, Top10List, login, mydate)

app_name = "index"  # URL namespace
# namespace = 'index'
urlpatterns = [
    path("", IndexTemplate.as_view(), name="index_home"),
    path("list/", ProductList.as_view(), name="index_list"),
    path("<year>/<int:month>/<slug:day>/", mydate, name="mydate"),
    path("<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("login/", login, name="login"),
    path(
        "test/",
        TemplateView.as_view(template_name="index/test2.html"),
        name="test2"),
    path(
        'test3/',
        TemplateView.as_view(template_name='index/test3.html'),
        name='test3'),
    path('top10', Top10List.as_view(), name='top10'),
    path(
        'books/<str:publisher>',
        PublisherBookList.as_view(),
        name='book_publisher')
]
