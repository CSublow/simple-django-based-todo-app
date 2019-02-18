# """django_todo URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.conf.urls import url
# from django.contrib import admin
# from todo.views import get_todo_list, create_an_item, edit_an_item, done_status

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', get_todo_list),
#     url(r'^add$', create_an_item),
#     # Breaking the url down below...
#     # The ?P stands for a regular expression following
#     # The <id> is the name of the value we want to pass into the function
#     # \d+ passes in any number of digits
#     url(r'^edit/(?P<id>\d+)$', edit_an_item),
#     # The url for done_status is very similiar to edit_an_item
#     url(r'^done/(?P<id>\d+)$', done_status),
# ]

"""Code Institute's github source code is below. Using because for some reason you was only getting 97% test coverage for views"""



"""django_todo URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo.views import get_todo_list, create_an_item, edit_an_item, toggle_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status)
]