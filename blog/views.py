from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *
import numpy as np
import pandas as pd
from io import StringIO
import re
import os
from sklearn import feature_extraction
import joblib
import json
# Create your views here.
def clusterin(file_link,nono):

    si = joblib.load('D:/ProjectFinal/mysite/modelfiles/si.pkl')
    f = pd.read_csv(file_link)
    if nono == 1:
        f = f
    else:
        f = f[si:si+100]
        si = si +101
        joblib.dump(si, 'D:/ProjectFinal/mysite/modelfiles/si.pkl')
    hoe = f['headline']
    h= []
    for i in hoe:
        h.append(i)
    keep_col = ['content']
    datas= f[keep_col]
    dataset = []
    lists = [[row[col] for col in datas.columns] for row in datas.to_dict('records')]
    for i in lists:
        for j in i:
            dataset.append(j)
    from sentence_transformers import SentenceTransformer, models
    word_embedding_model = models.Transformer('sagorsarker/bangla-bert-base', max_seq_length=256)
    ##joblib.dump(word_embedding_model, 'wem.pkl')
    ##word_embedding_model = joblib.load('wem.pkl')
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    embeddings = model.encode(dataset, show_progress_bar=True)
    km = joblib.load('D:/ProjectFinal/mysite/modelfiles/finalmodel6.pkl')
    new = km.predict(embeddings).tolist()

    output=[]
    clustered_sentences = [[] for i in range(6)]
    clustered_headlines = [[] for i in range(6)]
    for sentence_id, cluster_id in enumerate(new):
        clustered_sentences[cluster_id].append(dataset[sentence_id])
    for sentence_id, cluster_id in enumerate(new):
        clustered_headlines[cluster_id].append(h[sentence_id])
        
    return clustered_sentences,clustered_headlines
    


def index (request):
    clusters= Cluster.objects.all()


    context = {'clusters':clusters}
    return render(request, 'index.html',context)

def clustering(request):
    
    clustered_sentences,clustered_headlines = clusterin('D:/ProjectFinal/mysite/modelfiles/Authentic-48K.csv',20)

    for i, cluster in enumerate(clustered_sentences):
        newcluster = Cluster.objects.get(cluster_no = i)
        for j,ch in enumerate(clustered_headlines[i]):
            q = newcluster.article_set.create(headline = ch,content = cluster[j])
        print(i+1)
        print(cluster)
    
    cluster_list = Cluster.objects.all()
    for c in cluster_list:
        c.item_count = c.article_set.all().count()
        c.save()

    
    return render(request, 'index.html')



def cluster(request):
    text = request.POST["text"]
    from sentence_transformers import SentenceTransformer, models
    word_embedding_model = models.Transformer('sagorsarker/bangla-bert-base', max_seq_length=256)
    ##joblib.dump(word_embedding_model, 'wem.pkl')
    ##word_embedding_model = joblib.load('wem.pkl')
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    model = SentenceTransformer(modules=[word_embedding_model, pooling_model])
    e = []
    ems = model.encode(text, show_progress_bar=True)
    e.append(ems)
    km = joblib.load('D:/ProjectFinal/mysite/modelfiles/finalmodel6.pkl')
    few = km.predict(e).tolist()    
    return (detail(request,few[0]))

def prothomalo(request):

    clustered_sentences,clustered_headlines = clusterin('D:/ProjectFinal/mysite/blog/scraped_news.csv',1)

    for i, cluster in enumerate(clustered_sentences):
        newcluster = Pcluster.objects.get(cluster_no = i)
        for j,ch in enumerate(clustered_headlines[i]):
            q = newcluster.particle_set.create(headline = ch,content = cluster[j])

    
    cluster_list = Pcluster.objects.all()
    for c in cluster_list:
        c.item_count = c.particle_set.all().count()
        c.save()

    
    return render(request, 'prothomalo.html')

def viewprothomalo(request):
    clusters= Pcluster.objects.all()
    blusters= Cluster.objects.all()




    mylist = zip(clusters, blusters)
    context = {'mylist':mylist}
    return render(request, 'prothomalo.html',context)








def detail(request, c_no):
    try:
        cluster = Cluster.objects.get(cluster_no = c_no)
    except Cluster.DoesNotExist :
        raise Http404("The Item Does not Exist")
    return render(request, 'detail.html', {'cluster' : cluster})

def article(request, article_id):
    try:
        article = Article.objects.get(pk = article_id)
        cl = article.cluster
    except Article.DoesNotExist :
        raise Http404("The Item Does not Exist")
    
    context = {'article':article,'cluster':cl}    
    return render(request, 'article.html',context)


def pdetail(request, c_no):
    try:
        cluster = Pcluster.objects.get(pcluster_no = c_no)
    except Cluster.DoesNotExist :
        raise Http404("The Item Does not Exist")
    return render(request, 'pdetail.html', {'cluster' : cluster})




def particle(request, particle_id):
    try:
        particle = Particle.objects.get(pk = particle_id)
        c = particle.cluster
        cl = Cluster.objects.get(cluster_no = c.cluster_no)
    except Particle.DoesNotExist :
        raise Http404("The Item Does not Exist")
    context = {'particle':particle,'cluster':cl}   
    return render(request, 'particle.html', context)





