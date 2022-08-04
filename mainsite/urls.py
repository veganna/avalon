from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name="index-view"),
    path('contact/', views.contactView.as_view(), name="contact-view"),
    path('carousel/', views.carouselView.as_view(), name="carousel-view"),
    path('gallery/', views.galleryView.as_view(), name="gallery-view"),
    path('about/', views.aboutView.as_view(), name="about-view"),
    path('roadmap/', views.roadMapView.as_view(), name="roadmap-view"),
    path('faq/', views.faqView.as_view(), name="faq-view"),
    path('collection/', views.collectionView.as_view(), name="collection-view"),
    path('collection/<int:id>', views.collectionItemView.as_view(), name="collection-item-view"),
    path("terms-of-use/", views.termsView.as_view(), name= "terms-view"),
    path("privacy-policy/", views.policyView.as_view(), name= "policy-view"),
]