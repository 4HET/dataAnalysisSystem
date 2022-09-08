from pprint import pprint
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from . import dataTojson, Semantic_similarity
from django.template.defaulttags import register
import time
import pymysql
import pprint
import json
from . import Affective_analysis
from . import Review_c
from . import Word_vec

def mysql(sql, ty=0):
    conn = pymysql.connect(host="localhost", user="root", port=3306, passwd="123456", database="sheji")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    if ty==1:
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    else:
        cur.close()
        conn.close()
        return



def main(request):
    return render(request, 'index.html')


def data_preview(request):
    if request.method=='GET':
        file_id=request.GET.get('file_id')
        data = dataTojson.file_to_json(file_id)
        sql = 'SELECT file_name FROM file_info WHERE file_id="{}";'.format(file_id)
        file_name = mysql(sql, 1)[0][0]
        print(json.loads(data))
        context = {
            'data': data,
            'file_name': file_name,
        }
        return render(request, 'data_preview.html', context)


@register.filter
def get_range(value):
    return range(value)


def get_file_list(user_id):
    sql = 'SELECT file_name, file_id FROM file_info WHERE file_user="{}";'.format(user_id)
    file_data = list(mysql(sql, 1))
    dict1 = {}
    for i in range(len(file_data)):
        dict1[str(i)] = {}
        dict1[str(i)]['file_name'] = file_data[i][0]
        dict1[str(i)]['file_id'] = file_data[i][1]
    context = {
        'data': dict1,
        'file_num': len(file_data),
    }
    return context


def data_list(request):
    context = {}
    # user_id = request.session.get("user_id")
    user_id = 123
    if request.method=="POST":
        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("没有上传文件")
        houzhui = str(myFile.name).split(".")[-1]
        num = int(time.time())
        with open("DataAnalysis/per_data/{}.{}".format(str(user_id)+str(num), houzhui), "wb") as fi:
            for chunk in myFile.chunks():
                fi.write(chunk)
        sql = 'insert into file_info(file_name, file_id, file_user) values("{}", "{}", "{}");'.format(myFile.name, str(user_id)+str(num), user_id)
        print(sql)
        mysql(sql)
        context = get_file_list(user_id)
        request.FILES['myfile'] = None
        return redirect('../data_list')
    else:
        context = get_file_list(user_id)
        return render(request, 'data_list.html', context)


def file_rename(request):
    if request.method=="POST":
        file_name = request.POST["rename"]
        file_id = request.POST["file_id"]
        sql = 'UPDATE file_info SET file_name="{}" WHERE file_id={};'.format(file_name, file_id)
        mysql(sql)
        return redirect('../data_list')
    else:
        return redirect('../data_list')


def file_delet(request):
    if request.method=="POST":
        file_id = request.POST["file_id"]
        sql = 'DELETE FROM file_info WHERE file_id={};'.format(file_id)
        mysql(sql)
        return redirect('../data_list')
    else:
        return redirect('../data_list')

def affective_analysis(request):
    if request.method=="POST":
        file_id = request.POST["file_id"]
        file_name = request.POST["file_name"]
        new_file_id = Affective_analysis.analysis(file_id, file_name)
        return JsonResponse({"new_file_id": new_file_id},safe=False)
    else:
        return redirect('../data_list')



def word_vec(request):
    if request.method=="POST":
        file_id = request.POST["file_id"]
        file_name = request.POST["file_name"]

        Word_vec.word_vec(file_id, file_name)
        return redirect('../data_list')
    else:
        return redirect('../data_list')

def semantic_similarity(request):
    if request.method=="POST":
        file_id = request.POST["file_id"]
        file_name = request.POST["file_name"]

        Semantic_similarity.semantic_similarity(file_id, file_name)
        return redirect('../data_list')
    else:
        return redirect('../data_list')

def review_c(request):
    if request.method=="POST":
        file_id = request.POST["file_id"]
        file_name = request.POST["file_name"]

        Review_c.review_c(file_id, file_name)
        return redirect('../data_list')
    else:
        return redirect('../data_list')