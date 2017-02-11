from django.shortcuts import render, HttpResponseRedirect


def index(request):
    return render(request, 'dank_app/index.html')


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        # todo query pass to nathen
        # nathen will return a context d
        responce = "output would go here"
        context_dict = {"query": query,
                        "responce": responce}
        return render(request, 'dank_app/search.html', context_dict)
    else:
        return HttpResponseRedirect('/')
