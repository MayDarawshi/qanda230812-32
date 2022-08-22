from aifc import Error
from django.http import HttpResponse,JsonResponse
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, teachersForm
from django.core import serializers
import json
import markdown2
import bleach
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(response):
    return HttpResponse("<h1>hiii</h1>")


def home(response):
    return render(response, 'home.html', {})


def about_us(response):
    return render(response, 'about_us.html', {})


def adminPage(response):
    return render(response, 'admin.html', {})


# def profile(response,email):
#     return HttpResponse("<h1>%s</h1>"%email )


def register(response):
    return render(response, 'register.html', {})


def login(response):
    return render(response, 'login.html', {})


def signup_teacher(response):
    form = CreateUserForm()
    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(response, 'signup_teacher.html', {'form': form})


def signup_user(response):
    form = UserCreationForm()
    return render(response, 'signup_user.html', {"form": form})


def pull_teachers_info(response):
    all_teachers = teachers.objects.all
    return render(response, 'pull_teachers_info.html', {"all": all_teachers})


def teachers_names(response):
    all_teachers = teachers.objects.all()
    return render(response, 'teachers_names.html', {"all": all_teachers})


# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)

#     return conn


# # it will create a databse with name sqlite.db
# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()
# connection.close()

# table_query = '''CREATE TABLE questions
#                (question,difficulty,grade,type,author,q_image=)'''

# cursor.execute(table_query)
# connection.commit()
# connection.close()   


def all_questions(response):
    all_questions = questions.objects.all
    return render(response, 'all_questions.html', {"all": all_questions})


def subjects(response):    
    all_questions = questions.objects.all
    return render(response, 'subjects.html', {"all": all_questions})


def index(request):
    context = {}
    context['questions'] = questions.objects.all()
    return render(request, 'index.html', context)

def add_question(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            question = request.POST.get('question')
            difficulty= request.POST.get('difficulty')
            grade=request.POST.get('grade')
            type=request.POST.get('type')
            id=request.POST.get('id')
            q = questions(question=question,title=title ,difficulty=difficulty,grade=grade,type=type,id=id)
            print(q)

            q.save()
            # return redirect(view_question, q.qid, q.slug)
        except Exception as e:
            return render(request, 'add_question.html', { 'error': 'Something is wrong with the form!' })
    return render(request, 'add_question.html', {})

def view_question(request, qid, qslug):
    context = {}
    question = questions.objects.get(qid=qid, slug=qslug)

    # assuming obj is a model instance
    question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']
    question_json['qid'] = question.qid
    question_json['question'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    question_json['difficulty'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    question_json['type'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    question_json['grade'] = bleach.clean(markdown2.markdown(question_json['question']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    context['question'] = question_json
    context['answers'] = []
    answers = Answer.objects.filter(qid=qid)
    for answer in answers:
        answer.answer_text = bleach.clean(markdown2.markdown(answer.answer_text), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
        context['answers'].append(answer)
    return render(request, 'view_question.html', context)


def take_test(response):
    return render(response, 'take_test.html', {})



def teacher_profile(request,id):
    all_questions_for_teacher = questions.objects.filter(id=id)
    return render(request, 'teacher_profile.html', {"all": all_questions_for_teacher})
    

