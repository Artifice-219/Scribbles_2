from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import Letter
from .forms import LetterForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Lor the best programmer")

# for the login page
def loginpage(request):
    return render(request,'loginpage.html')

# for the signup page
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success')  
    else:
        form = UserForm() 

    return render(request,'signup.html', {'form' : form} )

# for the dashboard
def user_dashboard(request):
    return render(request, 'user-dashboard.html')

# for the success dialog
def success(request):
    return render(request, 'success.html')



# JESS STRUCTURE.
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Letter
# from .forms import LetterForm

# List all letters
def letter_list(request):
    letters = Letter.objects.all()
    return render(request, 'template/DFEDSDFC.html', {'letters': letters})

# Create a new letter
def letter_create(request):
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('letter_list')
    else:
        form = LetterForm()
    return render(request, 'template/create.html', {'form': form})

# Update an existing letter
def letter_update(request, pk):
    letter = get_object_or_404(Letter, pk=pk)
    if request.method == "POST":
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return redirect('letter_list')
    else:
        form = LetterForm(instance=letter)
    return render(request, 'template/create.html', {'form': form})

# Delete a letter
def letter_delete(request, pk):
    letter = get_object_or_404(Letter, pk=pk)
    if request.method == "POST":
        letter.delete()
        return redirect('letter_list')
    return render(request, 'template/letter-detail.html', {'letter': letter})
