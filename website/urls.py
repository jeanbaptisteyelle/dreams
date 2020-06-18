from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('about', views.about, name='about'),

    path('service', views.service, name='service'),

    path('blog', views.blog, name='blog'),

    path('single-blog', views.single_blog, name='single blog'),

    path('project', views.project, name='project'),

    path('appartment', views.appartment, name='appartment'),

    path('elements', views.elements, name='elements'),

    path('contact', views.contact, name='contact'),

]