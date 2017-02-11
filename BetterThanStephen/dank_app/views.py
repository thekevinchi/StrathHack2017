from django.shortcuts import render, HttpResponseRedirect
from query_functions import find_keywords, query_db
from django.contrib.auth.models import User
from dank_app.models import UserProfile

def index(request):
    return render(request, 'dank_app/index.html')

def search(request):
    if request.method == 'GET':
        print
        user = User.objects.get(username='bob')
        user_p = UserProfile.objects.get(user_account=user)

        query = request.GET.get('query', '')
        keywords = find_keywords(query)
        response = query_db(user_p, keywords)

        context_dict = {"query": query,
                        "response": response}
        return render(request, 'dank_app/search.html', context_dict)
    else:
        return HttpResponseRedirect('/')

def result(request):
    result_string = request.GET['result_string']
    keywords = find_keywords(result_string)
    
    print("result_string is: {0}".format(result_string))
    print("keywords are: {0}".format(keywords))

    query_db(keywords)
	
    return render(request, 'dank_app/index.html')

def speech(request):
    return render(request, 'dank_app/speech-demo.html')
