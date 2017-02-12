from math import sin, pi, cos

from django.shortcuts import render, HttpResponseRedirect
from query_functions import find_keywords, query_db
from django.contrib.auth.models import User
from dank_app.models import UserProfile, Payments


def index(request):
    if request.user.is_active:
        user = request.user
        all_payments = Payments.objects.filter(user=user.userprofile)
        total_to_be_payed = 0
        payments_recived = 0
        for payment in all_payments:
            if payment.paid:
                payments_recived += payment.amount
            total_to_be_payed += payment.amount

        percent_paid = int((float(payments_recived) / total_to_be_payed) * 100)
        graph_path = pos(percent_paid)
        context_dict = {'user': user,
                        'percent_paid': percent_paid,
                        'graph_path': graph_path,
                        'payments_recived':payments_recived,
                        'total_to_be_payed':total_to_be_payed,}
        print context_dict
        return render(request, 'dank_app/index.html', context_dict)
    context_dict = {'user': None}
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
            context_dict = {'user': user, }
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


def info(request):
    if request.user.is_active:
        user = request.user
        all_payments = Payments.objects.filter(user=user.userprofile)
        total_to_be_payed = 0
        payments_recived = 0
        for payment in all_payments:
            if payment.paid:
                payments_recived += payment.amount
            total_to_be_payed += payment.amount

        percent_paid = int((float(payments_recived) / total_to_be_payed) * 100)
        graph_path = pos(percent_paid)
        context_dict = {'user': user,
                        'percent_paid': percent_paid,
                        'graph_path': graph_path,
                        'payments_recived':payments_recived,
                        'total_to_be_payed':total_to_be_payed,}
        print context_dict
        return render(request, 'dank_app/info.html', context_dict)
    else:
        return HttpResponseRedirect('/')


def faq(request):
    if request.user.is_active:
        user = request.user
    else:
        user = None
    context_dict = {'user': user}
    return render(request, 'dank_app/faq.html', context_dict)


def pos(x):
    # you need to do "from math import *" because I'm a lazy bastard
    if x >= 75:
        return "M 0.5 0.5 0.5 0 A 0.5 0.5 0 0 1 %f %f z" % (
        (sin((100 - x) / 100.0 * 2 * pi) + 1) / 2, (1 - cos((100 - x) / 100.0 * 2 * pi)) / 2)
    elif x >= 50:
        res = "M 0.5 0.5 0.5 0 A 0.5 0.5 0 0 1 1 0.5"
        res += "M 0.5 0.5 1 0.5 A 0.5 0.5 0 0 1 %f %f" % (
        (sin((100 - x) / 100.0 * 2 * pi) + 1) / 2, (1 - cos((100 - x) / 100.0 * 2 * pi)) / 2)
    elif x >= 25:
        res = "M 0.5 0.5 0.5 0 A 0.5 0.5 0 0 1 1 0.5 M 0.5 0.5 1 0.5 A 0.5 0.5 0 0 1 0.5 1"
        res += "M 0.5 0.5 0.5 1 A 0.5 0.5 0 0 1 %f %f" % (
        (sin((100 - x) / 100.0 * 2 * pi) + 1) / 2, (1 - cos((100 - x) / 100.0 * 2 * pi)) / 2)
    else:
        res = "M 0.5 0.5 0.5 0 A 0.5 0.5 0 0 1 1 0.5 M 0.5 0.5 1 0.5 A 0.5 0.5 0 0 1 0.5 1 M 0.5 0.5 0.5 1 A 0.5 0.5 0 0 1 0 0.5"
        res += "M 0.5 0.5 0 0.5 A 0.5 0.5 0 0 1 %f %f" % (
        (sin((100 - x) / 100.0 * 2 * pi) + 1) / 2, (1 - cos((100 - x) / 100.0 * 2 * pi)) / 2)
    res += ' z'
    # this will return a svg drawing that you put into the d attribute
    return res
