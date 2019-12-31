from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic import View # 通用类视图 as_view的使用
from .models import cateType,UserInfo
import json,re
from django.core import serializers

class asyData(View):
    """异步数据获取"""
    def get(self,request):
        data = {}
        cid = request.GET.get('cid',None)
        catedata = cateType.objects.get(id=cid)
        userisdf = UserInfo.objects.filter(type=cid, is_default=1)
        print(userisdf)
        userdf = UserInfo.objects.filter(is_default=0)
        def object_to_json(obj):
            return dict([(kk, obj.__dict__[kk]) for kk in obj.__dict__.keys() if kk != "_state"])
        data["cate"]=object_to_json(catedata)
        data["userisdf"] = json.loads(serializers.serialize("json", userisdf))
        data["userdf"] = json.loads(serializers.serialize("json", userdf))
        return JsonResponse(data,safe=False)

class newYear(View):
    """新年活动类"""
    def get(self,request):
        """报名展示页"""
        cate = cateType.objects.all().order_by("-index")
        # isdata = UserInfo.objects.filter(is_default=1)
        # otdata = UserInfo.objects.filter(is_default=0)
        # con = {"otdata":otdata,"isdata":isdata,"cate":cate}
        con = {"cate":cate}
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
        ret = re.match(r"^1[35678]\d{9}$", phone)
        if ret is None:
            return HttpResponse("请输入正确的手机号")
        user = UserInfo.objects.filter(phone=phone)
        if user:
            return HttpResponse("你已经注册")
        UserInfo.objects.create(name=name,phone=phone)
        return HttpResponse("尊敬的%s 先生/女士，您的信息已成功登记,请等待抽奖"%(name))