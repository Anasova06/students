from django.shortcuts import render , redirect , get_object_or_404
from .models import Student
from .forms import StudentForm
def home(request):
    return render(request,'home.html')
def student(request):
    students = Student.objects.filter(is_active=True)
    return render(request, 'student.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()

    return render(request, 'student_list.html', {'form': form})
def student_info(request,pk):
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}
    return render(request, 'student_info.html', context)

def student_info_update(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'student_info_update.html', context)


def student_info_delete(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student')
    else:
        return render(request, 'student_info_delete.html')

