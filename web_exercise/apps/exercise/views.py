from django.shortcuts import render
from django.views.generic import DetailView, View


# Create your views here.

# 首页
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from apps.exercise.models import Part


class index(View):
    def get(self, request):
        action_list = Part.objects.all()
        paginator = Paginator(action_list,6)
        page = int(request.GET.get("page",1))
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        # 格式是bootstrap-table要求的格式

        return render(request, "index.html",{'contacts':contacts})


# 部位
def part(request):

    return render(request, "part_detail.html")


class IndexDetail(DetailView):
    model = Part
    pk_url_kwarg = 'id'
    template_name = 'part_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        shoulder = self.get_object()
        kwargs["my_shoulder"] = Part.objects.filter(title=shoulder.title, pic=shoulder.pic)
        return super().get_context_data(**kwargs)

