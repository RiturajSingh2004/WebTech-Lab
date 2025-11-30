from django.shortcuts import render, redirect
from .forms import StudentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('success', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'students/register.html', {'form': form})

def success(request, student_id):
    from .models import Student
    student = Student.objects.get(id=student_id)
    return render(request, 'students/success.html', {'student': student})
