#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100,verbose_name='书名')
    description = models.CharField(max_length=300, blank=True, verbose_name='简介')
    book_author = models.ForeignKey('Author',verbose_name='作者', on_delete=models.CASCADE, blank=True, null=True)
    book_lever = models.DecimalField(default=0, max_digits=2, decimal_places=1,verbose_name='等级', help_text = '最大值为9.9',)
    book_url = models.URLField(blank=True, max_length=100, verbose_name='链接')
    class_name = models.CharField('类别', max_length=100, blank=True, )
    thoughts = models.TextField('读后感', max_length=3000, blank=True, )
    def __str__(self):
        return self.book_name
    class Meta:
        #显示model名字
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ('-book_lever',)
    

class Author(models.Model):
    author_name = models.CharField(max_length=200, verbose_name='姓名')
    sex = models.BooleanField(verbose_name='性别', max_length=1,default=0, choices=((0, '男'),(1, '女'),))
    valuation = models.CharField(blank=True, max_length=400, verbose_name='评价')
    '''
    books = models.ManyToManyField(Book, 
                                through='Relationship',
                                through_fields=('author', 'book'))
    '''
    books = models.ForeignKey(Book, verbose_name='书籍', on_delete=models.CASCADE, blank=True, null=True)
    best_books = models.ForeignKey(Book, verbose_name='代表作',on_delete=models.CASCADE, null=True, blank=True,related_name='代表作', )
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    def __str__(self):
        return self.author_name 

    class Meta():
        verbose_name = '作者'
        verbose_name_plural = verbose_name

class Person(models.Model):
    name = models.CharField('姓名', max_length=100)
    sex = models.BooleanField('性别',max_length=1,default=0, choices=((0,'男'),(1,'女')))
    valuation = models.CharField(blank=True, max_length=400, verbose_name='评价')
    power = models.IntegerField('战斗力',blank=None, help_text='最多为100')
    intelligence = models.IntegerField('智力',blank=None, help_text='最多为100')
    ref_book = models.ForeignKey(Book, verbose_name = '相关书籍',on_delete=models.CASCADE,)
    ref_author = models.ForeignKey(Author, verbose_name='相关作者', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name 

    class Meta():
        verbose_name = '人物'
        verbose_name_plural = verbose_name 


 
