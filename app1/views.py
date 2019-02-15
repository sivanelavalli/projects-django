from django.shortcuts import render,redirect
from .models import Employee


def showIndex(request):
    qs = Employee.objects.all()
    return render(request,"index.html",{"data":qs})


def saveDetails(request):
    idno = request.POST.get("t1")
    name = request.POST.get("t2")
    dob = request.POST.get("t3")
    doj = request.POST.get("t4")
    gender = request.POST.get("t5")
    contactno = request.POST.get("t6")
    email = request.POST.get("t7")
    designation = request.POST.get("t8")
    salary = request.POST.get("t9")
    image = request.FILES["t10"]

    Employee(idno=idno,name=name,dob=dob,doj=doj,gender=gender,contactno=contactno,email=email,designation=designation,salary=salary,image=image).save()

    qs = Employee.objects.all()

    return render(request,"index.html",{"message":"Employee Details Saved","data":qs})


def showEmp(request):
    idno = request.POST.get("idno")
    qs = Employee.objects.filter(idno=idno)
    return render(request,"emp_details.html",{"data":qs})


def delEmp(request):
    idno = request.POST.get("idno")
    qs = Employee.objects.filter(idno=idno)
    return render(request, "del_details.html", {"data": qs})


def conformDel(request):
    idno = request.POST.get("idno")
    Employee.objects.filter(idno=idno).delete()
    return redirect('/index/')