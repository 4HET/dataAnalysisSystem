from django.contrib import admin
from django.urls import path, include,re_path
# from django.conf.urls import url
from . import views
# from DataAnalysis.myData import views

urlpatterns = [
    re_path(r'^$', views.main),
    path('data_preview/', views.data_preview),
    path('data_list/', views.data_list),
    path('rename/', views.file_rename),
    path('delet/', views.file_delet),
    #情感分析
    path('affective_analysis/', views.affective_analysis),
    #词向量表示
    path('word_vec/', views.word_vec),
    #词义相似度
    path('semantic_similarity/', views.semantic_similarity),
    #评论观点抽取
    path('review_c/', views.review_c),

    path('', include("da.urls")),
    # path('myData/', include(("myData.urls", "myData"))),
    path('', include("myData.urls")),
]
