from django.db import models
from django.utils.text import slugify

# Create your models here.





class users(models.Model):
    user_name=models.CharField(max_length=100)
    grade=models.CharField(max_length=7)
    password=models.CharField(max_length=16)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    school=models.CharField(max_length=50)   
    

    def __str__(self) -> str:
        return super().__str__()

class teachers(models.Model):
    user_name=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    password=models.CharField(max_length=16)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self) -> str:
        return super().__str__()


class reports(models.Model):
    user_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    dis=models.CharField(max_length=500)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)

    def __str__(self) -> str:
        return super().__str__()


class questions(models.Model):
    question=models.CharField(max_length=10000)
    difficulty=models.CharField(max_length=7)
    grade=models.CharField(max_length=2)
    type=models.CharField(max_length=25)
    title=models.CharField(max_length=100)


    # q_image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self) -> str:
        return super().__str__()

class Answer(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(questions, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=50000)
    posted_by = models.TextField(max_length=20)
    # q_image=models.ImageField(null=True,blank=True,upload_to="images/")

    def __str__(self) -> str:
        return super().__str__()

