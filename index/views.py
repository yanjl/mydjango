from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Max, Min, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DeleteView, ListView, TemplateView

from .forms import ProductForm, ProductModelForm
from .models import Author, Book, Product, Publisher


# Create your views here.
def home_page(request):
    # return HttpResponse("<h1> you are a student<h1>")
    # 绝对路径
    return redirect("http://127.0.0.1/user/")


def mydate(request, year, month, day):
    return HttpResponse(f"{year}-{str(month)}-{str(day)}")


class ProductList(ListView):
    # template_name = "index/list.html"
    # context_object_name = "books"
    queryset = Book.objects.annotate(Count('authors'))
    model = Book


class Top10List(ListView):
    # template_name = 'index/top10.html'
    # context_object_name = 'publishers'
    model = Publisher

    # queryset = Publisher.top_ten_books

    # def get_queryset(self):
    #     return self.top_ten_books()
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['books'] = Publisher.objects..top_ten_books
    #     return context


class PublisherBookList(ListView):
    template_name = 'index/book_list.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(
            Publisher, name=self.kwargs['publisher'])
        # Book.objects.annotate(Count('authors'))
        return Book.objects.filter(publisher=self.publisher).annotate(
            Count('authors'))


class IndexTemplate(LoginRequiredMixin, TemplateView):
    template_name = "index/index.html"
    login_url = "/index/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
        # return super().get_context_data(**kwargs)


class ProductDetail(DeleteView):
    template_name = "index/detail.html"
    context_object_name = "book"
    model = Book

    # get_queryset 获取URL中的数据 self.kwargs['name'] or self.kwargs.get('name', default='x')
    # get_context_data 设置HTML模板中的其它变量
    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['authors'] = Book.objects.get(id=id).authors.all()
        return context

    # def get_object(self, queryset=None):
    #     obj= super().get_object(queryset=queryset)
    #     obj.last_accessed=timezone.now()
    #     obj.save()
    #     return obj


def login(request):
    if request.method == "GET":
        product = ProductModelForm()
        return render(request, "index/login.html", locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            product.save()
            # name = product.cleaned_data['name']
            # type = product.cleaned_data['type']
            # Product(name=name, type=type).save()
            return redirect("/index/list/")
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, "index/login.html", locals())
