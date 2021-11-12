from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'wordCounter.html')


def counter(request):
    #post metodu olarak ayarladığımız için GET metodu yerine POST olarak değiştirdik.
    words = request.POST['text']
    #text areada verdiğimiz isim buydu:
    wordCount = len(words.split())
    return render(request,'counter.html', {'amount': wordCount})
