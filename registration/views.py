from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import Student1
from registration.models import Student1


"""
def registration(request):
    return HttpResponse("Welcome to the registration!")

def mypage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
# Create your views here.
"""
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())

def dashboard(request):
  data=Student1.objects.all();
  context = {'data':data}
  return render(request, 'dashboard.html',context)


@csrf_exempt
def addstudent1(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')



        obj1 = Student1(fullname=fullname,email='email')
        obj1.save()

    data = Student1.objects.all()
    context = {'data': data}
    return render(request, 'dashboard.html',context)




def editstudent1(request,id):
  data = Student1.objects.get(id=id);
  context = {'data': data}
  return render(request, 'updatestudent.html', context)



def deletestudent1(request, id):
    deletestudent1 = Student1.objects.get(id=id)
    deletestudent1.delete()
    return redirect('/dashboard')



def updatestudent1(request,id):
  if request.method == 'POST':
    name = request.POST.get('fullname')
    email = request.POST.get('email')


    #modify the student details based on the student id given
    editstudent1 = Student1.objects.get(id=id)

    editstudent1.fullname=name
    editstudent1.email=email

    editstudent1.save()
  return redirect('/dashboard')





