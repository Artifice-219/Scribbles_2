# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, Http404
from .forms import UserForm, LetterForm, login_form
from .models import Letter
import json
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

def letter_create(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            print("Letter saved successfully")
            return redirect('user-dashboard')
        else:
            print("Form errors: ", form.errors)
    else:
        form = LetterForm()

    return render(request, 'user-dashboard.html', {'form': form})



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
@login_required
def user_dashboard(request):
    # fetching user details
    user = request.user
    # fetching all the letters in the database
    letters = Letter.objects.all()
    dashboard_data = {
        'user_profile' : {
            'username' : user.username
        },
        'letters':letters
    }
    # passing details to the dashboard
    return render(request, 'user-dashboard.html', {'dashboard_data':dashboard_data, 'letters':letters})

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
@login_required
# views.py


@csrf_exempt
def update_letter(request, letter_id):
    if request.method == 'POST':
        letter = get_object_or_404(Letter, id=letter_id)
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return redirect('user-dashboard')
        else:
            return redirect('user-dashboard')





# Delete a letter
@csrf_exempt
@require_http_methods(["DELETE"])

def delete_letter(request, letter_id):
    try:
        letter = Letter.objects.get(id=letter_id)
        letter.delete()
        return JsonResponse({"message": "Letter deleted successfully"}, status=200)
    except Letter.DoesNotExist:
        raise Http404("Letter not found")
    


def get_letter(request, letter_id):
    try:
        letter = Letter.objects.get(id=letter_id)
        data = {
            'id': letter.id,
            'title': letter.title,
            'recipient': letter.recipient,
            'content': letter.content,
        }
        return JsonResponse({'letter': data})
    except Letter.DoesNotExist:
        return JsonResponse({"message": "Letter not found"}, status=404)

