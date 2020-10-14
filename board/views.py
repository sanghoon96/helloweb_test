from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from pymongo import MongoClient

# Create your views here.
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://192.168.219.128:27017/')  as client:
        mydb = client.mydb
        result = list(mydb.worknet.find({}))			# get Collection with find()
        
        result_page = []
        for info in result:						# Cursor
            # del info(_id)
            temp = {'name':info['name'], 'tit':info['tit'], 'etc':info['etc']}
            result_page.append(temp)
            print(type(info), info)
        data['page_obj'] = result
        
    return render(request, 'board/listwithmongo.html', context=data)

# list 함수
def index(request):
    # dict 자료형 생성하기
    data = request.GET.copy()

    # MongoClient 객체 얻기
    client = MongoClient('mongodb://192.168.219.128:27017/')

    # DB 선택하기
    mydb = client.mydb

    # MOVIEBOARD 테이블 얻기
    result = list(mydb.MOVIEBOARD.find({}))
    data['page_obj'] = result

    return render(request, 'board/listmongo.html', context=data)

# listjob function
def listjob(request):
    # dict 자료형 생성하기
    data = request.GET.copy()

    # MongoClient 객체 얻기
    client = MongoClient('mongodb://192.168.219.128:27017/')

    # DB 선택하기
    mydb = client.mydb

    # WORKGOKR 테이블 얻기
    result = list(mydb.WORKGOKR.find({}))
    data['page_obj'] = result

    return render(request, 'board/listjob.html', context=data)