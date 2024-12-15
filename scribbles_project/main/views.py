# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserForm, LetterForm, login_form
from .models import Letter

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Lor the best programmer")

# for the login page
def loginpage(request):
    form = login_form()
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated User: {user}")  
            if user is not None:
                login(request, user)
                return redirect('user-dashboard')
            else:
                form.add_error(None, 'Invalid Username or Password')
        else:
            print(f"Form Errors: {form.errors}") 

    return render(request, 'loginpage.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the user with the hashed password
            return redirect('success')  # Redirect to a success page
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})


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
