import math

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.paginator import Paginator
from comp.models import Category, Comp


class IndexView(View):
    def get(self, request, cid=1, num=1):

        cid = int(cid)
        num = int(num)
        # 查询所有类别信息
        categorys = Category.objects.all().order_by('id')

        # 查询当前类别下的所有信息
        compList = Comp.objects.filter(category_id=cid).order_by('id')

        # 分页
        pager = Paginator(compList, 6)

        # 获取当前页
        page_compList = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

        # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pagelist = range(begin, end + 1)

        return render(request, 'index.html',
                      {'categorys': categorys, 'compList': page_compList, 'currentCid': cid, 'pagelist': pagelist,
                       'currentNum': num})


def recommend(func):
    def wrapper(detailView, request, compid, *args, **kwargs):

        # 将存放在cookie中的compid获取
        cookie_str = request.COOKIES.get('recommend', '')

        # 存放所有compid的列表
        compIdList = [coid for coid in cookie_str.split() if coid.strip()]

        # 最终需要获取的推荐竞赛
        compObjList = [Comp.objects.get(id=cpid) for cpid in compIdList if
                       cpid != compid and Comp.objects.get(id=cpid).category_id == Comp.objects.get(
                           id=compid).category_id][:3]

        # 将compObjList传递给get方法
        response = func(detailView, request, compid, compObjList, *args, **kwargs)

        # 判断compid是否存在compIdList中
        if compid in compIdList:
            compIdList.remove(compid)
            compIdList.insert(0, compid)
        else:
            compIdList.insert(0, compid)

        # 将compIdList中的数据存在cookie
        response.set_cookie('recommend', ' '.join(compIdList), max_age=7 * 24 * 60 * 60)

        return response

    return wrapper


class DetailView(View):
    @recommend
    def get(self, request, compid, recommendList=[]):
        compid = int(compid)

        # 根据id查询竞赛详情
        comp = Comp.objects.get(id=compid)

        return render(request, 'detail.html', {'comp': comp, 'recommendList': recommendList})
