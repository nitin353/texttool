"""
URL configuration for texttool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login',views.login,name="login"),
    path('footer',views.footer),
    path('change',views.change,name="change"),
    path('contact',views.contact,name="contact"),
    path('forget',views.forget,name="forget"),
    path('help',views.help,name="help"),
    path('index',views.index,name="index"),
    path('nn',views.nn),
    path('review',views.review,name="review"),
    path('base',views.base),
    path('new',views.new,name="faq"),
    path('review',views.review),
    path('help',views.help),
    path('contact',views.contact),
    path('register',views.register,name="register"),
     path('profile',views.profile,name="profile"),
     path('userprofile',views.userprofile, name="userprofile"),
     path('sidebar',views.sidebar),
     path('texttools',views.texttools,name="tools"),
      path('logout',views.logout,name="logout"),
      path('myblog',views.viewmyblogs,name="blogs"),
      path('detailblog/<int:id>',views.detailblog,name="detailblog"),
      path('textspeech',views.textspeech,name="texttospeech"),
      path('spellingchecker',views.spellingchecker,name="spellcheck"),
      path('wordcount',views.wordcount,name="wordcount"),
      path('texttoimage',views.texttoimage,name="image"),
      path('emailextract',views.emailextract,name="email"),
      path('urlextract',views.urlextract,name="url"),
      path('synonyms',views.synonyms,name="syn"),
      path('antonyms',views.antonyms,name="ant"),
      path('textconvertor',views.textconvertor,name="textconvert"),
      path('sentimental',views.sentimental,name="sentimental"),
       path('barcode',views.barcode,name="barcode"),
        path('imagepdf',views.imagepdf,name="img"),
        path('texttranslator',views.texttranslator,name="text"),
          path('texttool2',views.texttool2, name="texttool2"),
          path('news',views.news,name="news"),
          path('cyberbully',views.cyberbully,name="cyberbully"),
           path('qrgenrator',views.qrgenrator,name="qr"),
        path("speechlangtrans",views.speechlangtrans,name="speechlangtrans"),








]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
