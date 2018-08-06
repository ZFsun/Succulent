from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemail=models.EmailField()

    def __str__(self):
        return self.uname


    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = '用户数据'
'''
python manage.py startapp name
python manage.py makemigrations
python manage.py migrate
css 引入加 static/

{%extends 'basefoot.html%}
{%block head%}{%endblock head%}

post {%crsf_token%}
'''