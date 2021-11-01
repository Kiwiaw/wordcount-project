from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, "home.html")
def info(request):
    return render(request, "info.html")
def jaki(request):
    return render(request, "jaki.html")
def zium(request):
    return render(request, "zium.html")
def count(request):
    fulltest = request.GET["fulltext"]
    wordlist =fulltest.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add to the dictionary
            worddictionary[word]=1
    sort  =sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)



    return render(request,"count.html",{"fulltest":fulltest, "count":len(wordlist),
    "najwiecej":sort})
