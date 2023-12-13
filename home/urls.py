from django.contrib import admin
from django.urls import path, include
import settings
from django.conf.urls.static import static

from home.models import btech, pgd
from . import views

admin.site.site_header = "Admission Portal"
admin.site.site_title = "Welcome to Admission Portal"
admin.site.index_title = "Welcome to Admission Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('user', views.user, name='user'),
    path('search', views.search, name='search'),
    path('payment', views.payment, name='payment'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('btecha/<int:userid>', views.btecha, name="btecha"),
    path('bteche/<int:id>', views.bteche, name="bteche"),
    path('btechv/<int:id>', views.btechv, name="btechv"),
    path('Update/<int:id>', views.btechu, name='btechu'),
    path('mtechcsa/<int:userid>', views.mtechcsa, name="mtechcsa"),
    path('mtechcse/<int:id>', views.mtechcse, name="mtechcse"),
    path('mtechcsv/<int:id>', views.mtechcsv, name="mtechcsv"),
    path('mtechcsu/<int:id>', views.mtechcsu, name='mtechcsu'),
    path('mtechaia/<int:userid>', views.mtechaia, name="mtechaia"),
    path('mtechaie/<int:id>', views.mtechaie, name="mtechaie"),
    path('mtechaiv/<int:id>', views.mtechaiv, name="mtechaiv"),
    path('mtechaiu/<int:id>', views.mtechaiu, name='mtechaiu'),
    path('mscdfa/<int:userid>', views.mscdfa, name="mscdfa"),
    path('pgda/<int:userid>', views.pgda, name="pgda"),
    path('mscdfe/<int:id>', views.mscdfe, name="mscdfe"),
    path('mscdfv/<int:id>', views.mscdfv, name="mscdfv"),
    path('mscdfu/<int:id>', views.mscdfu, name='mscdfu'),
    path('pgde/<int:id>', views.pgde, name="pgde"),
    path('pgdv/<int:id>', views.pgdv, name="pgdv"),
    path('pgdu/<int:id>', views.pgdu, name='pgdu'),
    path("activate/<uidb64>/<token>", views.activate, name='activate'),

    #    path("activate/<uidb64>/<token>", views.activate, name='activate'),

    # path('mtechaia/<int:userid>',views.mtechaia,name="mtechaia"),
    # path('msca/<int:userid>',views.msca,name="msca"),
    # path('pgda/<int:userid>',views.pgda,name="pgda"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
