from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from user.models import UserInfo
from util.code import *


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self, request):
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        # 插入数据库
        user = UserInfo.objects.create(uname=uname, pwd=pwd)

        # 判断是否注册成功
        if user:
            # 将用户信息存放至session对象中
            request.session['user'] = user

            return HttpResponseRedirect('/user/center/')

        return HttpResponseRedirect('/user/register/')


class CheckUnameView(View):
    def get(self, request):
        # 获取请求参数
        uname = request.GET.get('uname', '')

        # 根据用户名去数据库中查询
        userList = UserInfo.objects.filter(uname=uname)

        flag = False

        # 判断是否存在
        if userList:
            flag = True

        return JsonResponse({'flag': flag})


class CenterView(View):
    def get(self, request):
        return render(request, 'center.html')


class LogoutView(View):
    def post(self, request):
        if 'user' in request.session:
            del request.session['user']

        return JsonResponse({'delflag': True})


class LoginView(View):
    def get(self,request):

        #获取请求参数
        red = request.GET.get('redirct','')

        return render(request,'login.html',{'redirect':red})

    def post(self,request):
        #1.获取请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        #2.查询数据库中是否存在
        userList = UserInfo.objects.filter(uname=uname,pwd=pwd)

        if userList:
            request.session['user'] = userList[0]

            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/login/')


class LoadCodeView(View):
    def get(self,request):
        img,str = gene_code()

        #将生成的验证码存放至session中
        request.session['sessionCode'] = str

        return HttpResponse(img,content_type='image/png')


class CheckCodeView(View):
    def get(self,request):
        #获取输入框中的验证码
        code = request.GET.get('code','')

        #获取生成的验证码
        sessionCode = request.session.get('sessionCode',None)

        #比较是否相等
        flag = code == sessionCode

        return JsonResponse({'checkFlag':flag})


