from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def index(request):
    #news data by API
    newsData = True
    newsResult = None
    newsSummary = None

    while(newsData):
        try:
            newsResult = requests.get("https://saurav.tech/NewsAPI/top-headlines/category/health/in.json")
            newsSummary = newsResult.json()['articles']
            newsData = False
        except:
            newsData = True


    # Latest count of covid for global
    data = True
    result = None
    globalSummary = None
    while(data):
        try:
            result = requests.get("https://api.covid19api.com/summary")
            globalSummary = result.json()['Global']
            globalCountries = result.json()['Countries']
            data = False
        except:
            data = True

    context ={
        'newsSummary' : newsSummary,
        'globalSummary': globalSummary,
        'globalCountries' : globalCountries,
    }
    return render(request, 'covidapp/index.html', context)

#countrywise data with API
def dataCountry(request):
    data = True
    result = None
    globalSummary = None
    while(data):
        try:
            result = requests.get("https://api.covid19api.com/summary")
            globalSummary = result.json()['Global']
            globalCountries = result.json()['Countries']
            data = False
        except:
            data = True

    context = {
        'globalSummary': globalSummary, 
        'globalCountries': globalCountries,
    }
    return render(request, 'covidapp/country.html', context)

def dataState(request):
    stateData = True
    stateResult = None
    stateSummary = None
    while (stateData):
        try:
            stateResult = requests.get("https://api.covid19india.org/data.json")
            stateAll = stateResult.json()['cases_time_series']
            stateSummary = stateResult.json()['statewise']
            stateData = False
        except:
            stateData = True

    context ={
        'stateSummary': stateSummary,
        'stateAll': stateAll,
    }
    return render(request, 'covidapp/state.html', context)    
