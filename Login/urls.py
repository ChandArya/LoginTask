from django.conf.urls import url
from . import views
appname='login'
urlpatterns=[
    #login
    url(r'^$',views.index,name='index'),
    #login/1/
    url(r'^(?P<user_id>[0-9]+)/$',views.login,name='login'),
    #login/store/
    url(r'^store/$',views.store,name='store'),
    #login/user/
    url(r'^user/$',views.userlogin,name='user'),
]