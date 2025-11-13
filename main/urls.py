from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('insights/', views.insights, name='insights'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('markets/', views.markets, name='markets'),
    path('news/', views.news, name='news'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('architecture/residential/', views.architecture_residential, name='architecture_residential'),
    path('architecture/commercial/', views.architecture_commercial, name='architecture_commercial'),
    path('architecture/hospitality/', views.architecture_hospitality, name='architecture_hospitality'),
    path('architecture/civic/', views.architecture_civic, name='architecture_civic'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('issues/tight-spaces/', views.issue_tight_spaces, name='issue_tight_spaces'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
]
