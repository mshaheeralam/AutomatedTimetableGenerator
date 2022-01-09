from django.contrib import messages
from django.core.files import File
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from BACKEND.scheduler import main
from .models import Course


# Create your views here.
def index(request):
    """
    THIS FUNCTION CREATES A COURSE CLASS OBJECT AND SENDS IT TO THE DATABASE
    """
    if request.method == "POST":
        c = Course()
        c.code = request.POST.get('code', '')
        c.instructor = request.POST.get('instructor', '')
        c.group = request.POST.get('group', '')
        c.credithour = request.POST.get('credithour', '')
        c.faculty = request.POST.get('faculty', '')
        if request.POST.get('lab', '') == 'on':
            c.lab = True
            c.lab_instructor = request.POST.get('lab_instructor', '')
        else:
            c.lab = False
        c = Course(code=c.code, instructor=c.instructor, group=c.group, credithour=c.credithour, faculty=c.faculty,
                   lab=c.lab, lab_instructor=c.lab_instructor)
        c.save()

        with open('BACKEND/test_files/text.txt', 'w') as f:
            myfile = File(f)
            myfile.write('{"Classrooms": {\n'
                         '\t"FES": ["FES MLH", "FES LH1", "FES LH2", "FES LH2", "FES LH3", "FES LH4"],\n'
                         '\t"FES LAB": ["FES PH LAB"],\n'
                         '\t"FCSE": ["FCSE MLH", "FCSE LH1", "FCSE LH2", "FCSE LH2", "FCSE LH3", "FCSE LH4"],\n'
                         '\t"FCSE LAB": ["FCSE OSP LAB", "FCSE PC LAB", "FCSE SE LAB"],\n'
                         '\t"FME": ["FME MLH", "FME LH1", "FME LH2", "FME LH2", "FME LH3", "FME LH4"],\n'
                         '\t"FMCE": ["FMCE MLH", "FMCE LH1", "FMCE LH2", "FMCE LH2", "FMCE LH3", "FMCE LH4"],\n'
                         '\t"FEE LAB": ["FEE LCA LAB", "FEE DLD LAB", "FEE MS LAB"],\n'
                         '\t"FEE": ["FEE MLH", "FEE LH1", "FEE LH2", "FEE LH2", "FEE LH3", "FEE LH4"],\n'
                         '\t"MGS": ["BB MLH"]},\n'
                         '"Classes": [\n')

            b = Course.objects.all()[0]

            if b.lab:
                temp = b.group.split()
                myfile.write(
                    f'\t{{"Subject": "{b.code}", "Type": "L", "Teacher": "{b.lab_instructor}", "Groups": ["{temp[0]}"')
                for i in temp[1:]:
                    myfile.write(f', "{temp[j]}"')
                myfile.write(f'], "Classroom": "{b.faculty} LAB", "Duration": "{3}"}}')
                for i in range(b.credithour):
                    temp = b.group.split()
                    myfile.write(
                        f',\n\t{{"Subject": "{b.code}", "Type": "P", "Teacher": "{b.instructor}", "Groups": ["{temp[0]}"')
                    for j in temp[1:]:
                        myfile.write(f', "{temp[j]}"')
                    myfile.write(f'], "Classroom": "{b.faculty}", "Duration": "{1}"}}')

            for a in Course.objects.all()[1:]:
                if b.credithour == 3 or b.credithour == 2:
                    Type = 'P'
                    duration = 1
                elif b.credithour == 1:
                    Type = 'L'
                    duration = 3

                if a.lab:
                    temp = a.group.split()
                    myfile.write(
                        f',\n\t{{"Subject": "{a.code}", "Type": "L", "Teacher": "{a.lab_instructor}", "Groups": ["{temp[0]}"')
                    for j in temp[1:]:
                        myfile.write(f', "{j}"')
                    myfile.write(f'], "Classroom": "{a.faculty} LAB", "Duration": "{3}"}}')
                for i in range(a.credithour):
                    temp = a.group.split()
                    myfile.write(
                        f',\n\t{{"Subject": "{a.code}", "Type": "{Type}", "Teacher": "{a.instructor}", "Groups": ["{temp[0]}"')
                    for j in temp[1:]:
                        myfile.write(f', "{j}"')
                    myfile.write(f'], "Classroom": "{a.faculty}", "Duration": "{duration}"}}')

            myfile.write(']\n}')
            myfile.closed
            f.closed

    return render(request, 'FRONTEND/index.html')


def generate(request):
    main()
    return render(request, 'FRONTEND/generate.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, 'FRONTEND/index.html', {'name': name})
        else:
            messages.error(request, 'Wrong Credentials!')
            return redirect('signin')
    return render(request, 'FRONTEND/signin.html')


def signout(request):
    logout(request)
    return redirect('signin')
