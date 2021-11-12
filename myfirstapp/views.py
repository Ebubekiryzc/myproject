from django.shortcuts import render, redirect
from django.http import HttpResponse
# Burası sqllite' da bulunan users tablosunu gösteriyor:
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

# burada yapılacak şey url' e atanacak şeydir.


def index(request):
    # return HttpResponse('<h1>Hey, welcome!</h1>')
    # context = {
    #     'name': 'Patrick',
    #     'age': 23,
    #     'nationality': 'Turkish',
    # }
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true= True
    # feature1.details = 'Our service is really quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true= True
    # feature2.details = 'Our service is really Reliable'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.is_true= False
    # feature3.details = 'Our service is easy to use'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true= True
    # feature4.details = 'Our service is really affordable'

    # features = [feature1, feature2, feature3, feature4]

    # sayfaya dinamik olarak içerik yollamak için bu şekilde map yapısı kullanırız ya dacontext yazarız direkt olarak
    # return render(request, "index.html", {'features':features})

    features = Feature.objects.all()

    return render(request, "index.html", {'features': features})


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeatPassword = request.POST["repeat-password"]

        if password == repeatPassword:
            # user zaten mevcut mu ?
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already on use.")
                # hata olursa tekrar register sayfasına yönlendiriyoruz.
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already on use.")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "The passwords not same.")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def counter(request):
    posts = [1, 2, 3, 4, 5, ' ebu ', ' meryem ', ' berkcan ', ' şeyma ']
    return render(request, 'counter.html', {'posts': posts})
