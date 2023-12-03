from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from.models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {'user': request.user})
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_information')
        else:
            return HttpResponse('error')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_information')
        else:
            return HttpResponse('error')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        data = User.objects.create_user(username=username, password=password)
        data.save()
        return redirect('login')
        

class UserInformationView(View):
    def get(self, request):
        departments = Department.objects.all()
        courses = Course.objects.filter(department__in=departments)
        return render(request, 'user_information.html', {'departments': departments, 'courses': courses})

    def post(self, request):
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        department_id = request.POST.get('department')
        department = Department.objects.get(pk=department_id)
        course_id = request.POST.get('course')
        course = Course.objects.get(pk=course_id)
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.getlist('materials_provide')

        Student.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            department=department,
            course=course,
            purpose=purpose,
            materials_provided=', '.join(materials_provide)
        )

        
        confirmation_message = "Order Confirmed"
        return render(request, 'user_information.html', {'confirmation_message': confirmation_message})


def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id)
    courses_data = [{'id': course.id, 'name': course.name} for course in courses]
    return JsonResponse(courses_data, safe=False)