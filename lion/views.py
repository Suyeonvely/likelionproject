from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Lion
# Create your views here.


# Create your views here.
def home(request):
    lions = Lion.objects
    #블로그 모든 글들을 대상으로
    lion_list=Lion.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(lion_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'lions':lions,'posts':posts})

def detail(request, lion_id):
    lion_detail = get_object_or_404(Lion, pk=lion_id)
    return render(request, 'detail.html', {'lion': lion_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    lion = Lion()
    lion.title = request.GET['title']
    lion.body = request.GET['body']
    lion.pub_date = timezone.datetime.now()
    lion.save()
    return redirect('/lion/' + str(lion.id))