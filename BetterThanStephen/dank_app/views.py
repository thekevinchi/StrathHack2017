from django.shortcuts import render, HttpResponseRedirect
from query_functions import find_keywords, query_db

def index(request):
    return render(request, 'dank_app/index.html')

def result(request):
    result_string = request.GET['result_string']
    keywords = find_keywords(result_string)
    
    print("result_string is: {0}".format(result_string))
    print("keywords are: {0}".format(keywords))

    query_db(keywords)
	
    return render(request, 'dank_app/index.html')

def speech(request):
    return render(request, 'dank_app/speech-demo.html')
