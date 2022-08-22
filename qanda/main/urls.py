from tokenize import String
from urllib.parse import urlencode
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.home,name="home"),
    path("about_us/",views.about_us,name="about_us"),
    path("adminPage/",views.adminPage,name="adminPage"),
    path('teacher_profile/<int:id>',views.teacher_profile,name="teacher_profile"),
    path("register/",views.register,name="register"),
    path("signup_teacher/",views.signup_teacher,name="signup_teacher"),
    path("signup_user/",views.signup_user,name="signup_user"),
    path("login/",views.login,name="login"),  
    path("pull_teachers_info/",views.pull_teachers_info,name="pull_teachers_info"),  
    path("teachers_names/",views.teachers_names,name="teachers_names"),  
    path("all_questions/",views.all_questions,name="all_questions"),  
    path("subjects/",views.subjects,name="subjects"),  
    path("take_test/",views.take_test,name="take_test"),  
    path("view_question/{int}",views.view_question,name="view_question"),  
    path("add_question/",views.add_question,name="add_question"),  
    path("index/",views.index,name="index"), 
     




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)