from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from .forms import Studentform

# Create your views here.
def student_list(request):
    student = Student.objects.all()
    context = {'students':student}
    return render(request,'index.html',context)

def student_view(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,"student_detail.html",{'students':student})

def update(request,pk):
    student = get_object_or_404(Student,pk=pk)
    form = Studentform(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'form.html',{'form':form})

def delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method=="POST":
        student.delete()
        return redirect('student_list')
    return render(request,'delete.html',{'object':student})

def create(request):
    form = Studentform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'form.html',{'form':form})

