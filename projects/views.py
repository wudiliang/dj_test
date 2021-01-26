from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#函数视图
# from django.views import View
#
#
# def index(request):
#
#     return HttpResponse("<h1>Hello,你好<h1>")

#类视图
from django.views import View


class IndexView(View):

    def get(self,request):
        return HttpResponse("<h1>Hello,get你好<h1>")

    def post(self,request):
        return HttpResponse("<h1>Hello,post你好<h1>")