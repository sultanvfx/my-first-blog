from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # '^$' means only an empty string will match is done by regular expression. name='post_list' -> is the name of the URL that will be used to identify the view.

]
