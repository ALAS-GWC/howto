from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # this is your new view
    return render(request, 'index.html')

def algebra1(request):
    return render(request, 'algebra1.html')

def algebra2trig(request):
    return render(request, 'algebra2-trig.html')

def apbio(request):
    return render(request, 'apbio.html')

def apecon(request):
    return render(request, 'apecon.html')

def apgov(request):
    return render(request, 'apgov.html')

def apphysics(request):
    return render(request, 'apphysics.html')

def apush(request):
    return render(request, 'apush.html')

def BC(request):
    return render(request, 'BC.html')

def bio(request):
    return render(request, 'bio.html')

def chem(request):
    return render(request, 'chem.html')

def comp(request):
    return render(request, 'comp.html')

def euro(request):
    return render(request, 'euro.html')

def geometry(request):
    return render(request, 'geometry.html')

def lit(request):
    return render(request, 'lit.html')

def physics(request):
    return render(request, 'physics.html')

def precalc(request):
    return render(request, 'precalc.html')

def world(request):
    return render(request, 'world.html')

def english(request):
    return render(request, 'english.html')

def math(request):
    return render(request, 'math.html')

def history(request):
    return render(request, 'history.html')

def college(request):
    return render(request, 'college.html')

def contact(request):
    return render(request, 'contact.html')

def science(request):
    return render(request, 'science.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
