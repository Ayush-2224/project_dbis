from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Student, College
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='student_login')  # Redirects to login if user is anonymous
def student_register(request):
    if request.method == 'POST':
        try:
            # Retrieve current user's username as roll_no
            roll_no = request.user.username
            username=request.user.username
            rank = request.POST.get('rank')
            c_name = request.POST.get('c_name')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            c_rank = request.POST.get('c_rank')
            xii_percentage = request.POST.get('xii_percentage')
            category = request.POST.get('category')
            nationality = request.POST.get('nationality')
            address = request.POST.get('address')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            # Create and save the Student instance
            student = Student(
                roll_no=roll_no,
                rank=rank,
                c_name=c_name,
                gender=gender,
                dob=dob,
                c_rank=c_rank,
                xii_percentage=xii_percentage,
                category=category,
                nationality=nationality,
                address=address,
                email=email,
                phone=phone
            )
            student.save()
            messages.success(request, "Student registered successfully!")
            return redirect('student_home')  # Redirect to the home page after successful registration
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {e}")
            return redirect('student_register')  # Redirect back to the registration page on error

    # If not POST, render the registration form
    return render(request, 'students/register.html')

def student_home(request):
    if request.user.is_anonymous:
        return redirect("student/login")
    return render(request, 'students/home.html')
def college_home(request): 
    if request.user.is_anonymous:
        return redirect("college/login")
    return render(request,'colleges/home.html')
def home(request):
    
    return render(request,'colleges/common_home.html')




def student_logout(request):
    logout(request)
    return redirect("student_login")


def student_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Create the User instance
                user = User.objects.create_user(username=username, password=password)
                user.save()

                messages.success(request, "Student registered successfully!")
                return redirect('student_login')  # Redirect to login page after registration
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'students/signup.html')




# Student login view
def student_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is associated with a Student
            if Student.objects.filter(username=user.username).exists():
                
                return redirect("student_home")  # Redirect after successful login
            else:
                return redirect ("common_home")
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'students/signup.html')

    return render(request, 'students/login.html')  # Render login page


# College login view
def college_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is associated with a College
            if College.objects.filter(college_id=user.username).exists():
                
                return redirect("college_home")  # Redirect after successful login
            else:
                return redirect ("common_home")
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'colleges/login.html')

    return render(request, 'colleges/login.html')  # Render login page


# College signup view
def college_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Create the User instance
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Additional college information can be added here if needed
                messages.success(request, "College registered successfully!")
                return redirect('college_login')  # Redirect to login page after registration
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'colleges/signup.html')


# College logout view
def college_logout(request):
    logout(request)
    return redirect("college_login")


@login_required(login_url='college_login')  # Redirects to college login if not authenticated
def college_register(request):
    if request.method == 'POST':
        try:
            # Retrieve current user's username as college_id
            college_id = request.user.username
            # Get data from form fields
            college_name = request.POST.get('college_name')
            college_type = request.POST.get('college_type')
            contact_no = request.POST.get('contact_no')
            email = request.POST.get('email')

            # Create and save the College instance
            college = College(
                college_id=college_id,
                college_name=college_name,
                college_type=college_type,
                contact_no=contact_no,
                email=email,
            )
            college.save()
            messages.success(request, "College registered successfully!")
            return redirect('college_home')  # Redirect to the home page after successful registration
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {e}")
            return redirect('college_register')  # Redirect back to the registration page on error

    # If not POST, render the registration form
    return render(request, 'colleges/register.html')
