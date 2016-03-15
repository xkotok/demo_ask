# -- coding: utf-8 --
from django.shortcuts import render
#, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from forms import AskForm, AnswerForm
# Create your views here.
# тестируем комменты на руском
def test(request, *args, **kwargs):
    return HttpResponse('OK')
def question(request, id_s, *args,  **kwargs):
    id_int = int(id_s)
#    quest = get_object_or_404(Question, id_s)
    try:
        quest = Question.objects.get(id=id_int)
    except Question.DoesNotExist:
        raise Http404
    form = AnswerForm()
    try: answer = Answer.objects.filter(question=id_int)
    except Answer.DoesNotExist:
        return render(request, 'question.html', {'title': quest.title, 'text': quest.text, 'form': form })
    return render(request, 'question.html', {'title': quest.title, 'text': quest.text, 'answer': answer, 'form':form })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save()
            url = quest.get_url()
            return HttpResponseRedirect(url)
    elif request.method == "GET":
        form = AskForm()
    else:
        raise Http404
    return render(request,  'ask.html', {'form': form })
def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = quest.get_url()
            return HttpResponseRedirect(url)
def index(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    quest = Question.objects.all()
    if request.path == '/popular/':
        url = reverse('popular')
        sort_str = '-rating'
    else:
        url = reverse('index')
        sort_str = '-id'
    quest = quest.order_by(sort_str)
    paginator = Paginator(quest, 10) # must be 10 
    paginator.baseurl = url + '?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {
        'question': page.object_list, 
        'paginator': paginator, 'page': page, 
    
    })
