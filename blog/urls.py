from django.conf.urls import url
from django.urls import path
from .views import *
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('clustering', views.clustering, name = 'clustering'),
    path('cluster', views.cluster, name = 'cluster'),
    path('prothomalo', views.prothomalo, name = 'prothomalo'),
    path('viewprothomalo', views.viewprothomalo, name = 'viewprothomalo'),
    path('<int:c_no>/', views.detail, name = 'detail'),
    path('article/<int:article_id>', views.article, name = "article"),
    path('particle/<int:particle_id>', views.particle, name = "particle"),
    ##path('<int:item_id>/', views.detail, name = 'detail'),
    ##path('add_model/', views.add_model, name = 'add_model'),



]