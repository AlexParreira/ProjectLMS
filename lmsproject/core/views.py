from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno, Curso, ItemConteudo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def welcome_page(request):
    student = request.user.aluno  
    courses = student.cursos_liberados.all()  
    
    return render(request, 'core/welcome_page.html', {'student': student, 'courses': courses})

def course_detail(request, course_id):
    student = request.user.aluno  
    course = Curso.objects.get(pk=course_id)
    
    return render(request, 'core/course_detail.html', {'student': student,'course': course})

def item_conteudo_detail(request, item_id):
    item = ItemConteudo.objects.get(pk=item_id)
    
    return render(request, 'core/item_conteudo_detail.html', {'item': item})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('welcome_page')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'core/student_login.html')