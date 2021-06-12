from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import *
# Create your views here.
def list(request):
    studlist = Student.objects.all()
    context = {'students': studlist}
    return render(request, 'student/list.html',context)


def form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, 'student/form.html',{'form':form})
    else:
        if id==0:
            form = StudentForm(request.POST)
        else:
            student =Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('list')
    


def delete(request,id):
    student = Student.objects.get(pk=id)
    if request.method=='POST':
        student.delete()
        return HttpResponseRedirect("/") 

    return render(request, 'student/delete.html' )


