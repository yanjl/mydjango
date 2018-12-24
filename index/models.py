import uuid

from django.db import models
from django.utils.functional import cached_property


# Create your models here.
class Product(models.Model):
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "产品信息"
        verbose_name_plural = "产品信息"
        permissions = (("visit_Product", "Can visit Product"), )

    def get_lengthest_name(self):
        pass


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'

    def __str__(self):
        return self.name

    @cached_property
    def top_ten_books(self):
        return self.book_set.order_by('-rating')[:10]


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=300)
    pages = models.IntegerField(verbose_name='页数')
    price = models.DecimalField('单价', max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, verbose_name='出版商')
    pubdate = models.DateTimeField(
        '出版日期',
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        ordering = ['-pubdate', 'name']


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        verbose_name = '书店'
        verbose_name_plural = '书店'

    def __str__(self):
        return self.name

    def user_directory_path(self, filename):
        return f'user_{self.user.id}/{filename}'
