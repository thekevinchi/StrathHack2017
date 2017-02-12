from django.shortcuts import render, HttpResponseRedirect
from query_functions import find_keywords, query_db
from django.contrib.auth.models import User
from dank_app.models import UserProfile, Payments


def index(request):
    if request.user.is_active:
        user = request.user
    else:
        user = None
    context_dict = {'user': user}
    return render(request, 'dank_app/index.html', context_dict)


def search(request):
    if request.user.is_active:
        user = request.user
        if request.method == 'GET':
            query = request.GET.get('query', '')
            keywords = find_keywords(query)
            response = query_db(user.userprofile, keywords)

            context_dict = {"query": query,
                            "response": response,
                            'user': user}
            return render(request, 'dank_app/search.html', context_dict)
    else:
        user = None
        if request.method == 'GET':
            ## no user query
            # query = request.GET.get('query', '')
            # keywords = find_keywords(query)
            # response = query_db(keywords)
            context_dict = {'user': user,}
                        # "query": query,
                        # "response": response,
                        # }
        return render(request, 'dank_app/search.html', context_dict)

    return HttpResponseRedirect('/')


def result(request):
    if request.user.is_active:
        user = request.user
    else:
        user = None
    context_dict = {'user': user}
    result_string = request.GET['result_string']
    keywords = find_keywords(result_string)

    print("result_string is: {0}".format(result_string))
    print("keywords are: {0}".format(keywords))

    query_db(keywords)

    return render(request, 'dank_app/index.html', context_dict)


def speech(request):
    if request.user.is_active:
        user = request.user
    else:
        user = None
    context_dict = {'user': user}
    return render(request, 'dank_app/speech-demo.html', context_dict)


def graph(request):
    if request.user.is_active:
        user = request.user
        all_payments = Payments.objects.filter(user=user.userprofile)
        total_to_be_payed =0
        payments_recived =0
        for payment in all_payments:
            if payment.paid:
                payments_recived += payment.amount
            total_to_be_payed += payment.amount


    else:
        user = None
    context_dict = {'user': user,}
                    # 'percnetage':}
    return render(request, 'dank_app/graph.html')


def faq(request):
    if request.user.is_active:
        user = request.user
    else:
        user = None
    context_dict = {'user': user}
    return render(request, 'dank_app/faq.html', context_dict)
