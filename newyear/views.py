from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View # 通用类视图 as_view的使用
from .models import cateType,UserInfo


class newYear(View):
    """新年活动类"""
    def get(self,request):
        """报名展示页"""
        cate = cateType.objects.all().order_by("-index")
        isdata = UserInfo.objects.filter(is_default=1)
        otdata = UserInfo.objects.filter(is_default=0)
        con = {"otdata":otdata,"isdata":isdata,"cate":cate}
        return render(request, "newyear/index.html", con)

    def post(self,request):
        """报名提交页"""
        print(request)
        data = {}
        data["name"] = request.POST.get('name',None)
        data["phone"] = request.POST.get('phone',None)
        user = User(**data)
        user.save()
        return HttpResponse("提交成功")

class User(View):
    """用户等级"""
    def get(self,request):
        return render(request,"newyear/user.html")
    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        user = UserInfo.objects.filter(phone=phone)
        if user:
            return HttpResponse("你已经注册")
        UserInfo.objects.create(name=name,phone=phone)
        return HttpResponse("报名成功")