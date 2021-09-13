from django.shortcuts import render,redirect

from django.views import View
from django.db.models import Q

from .models import Topic,Trend
from .forms import TopicForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        context     = {}

        if "search" in request.GET:
            search      = request.GET["search"]

            if search == "" or search.isspace():
                return redirect("bbs:index")

            search      = search.replace("　"," ").split(" ")
            searches    = [ w for w in search if w != "" ]

            query       = Q() 
            for w in searches:
                query &= Q(comment__contains=w)

            #(4)作ったクエリを実行
            context["topics"]   = Topic.objects.filter(query)
        else:
            context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if form.is_valid():
            print("OK")
            form.save()

        return redirect("bbs:index")

index   = BbsView.as_view()

class TrendView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["trends"]   = Trend.objects.all().order_by("-count")[:150]

        return render(request,"bbs/trend.html",context)

trend   = TrendView.as_view()


