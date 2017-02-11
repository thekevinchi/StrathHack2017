from django.shortcuts import render, HttpResponseRedirect


def index(request):
    return render(request, 'dank_app/index.html')

def speech(request):
    return render(request, 'dank_app/speech-demo.html')
