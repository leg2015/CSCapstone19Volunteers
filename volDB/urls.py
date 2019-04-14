from django.conf.urls import url
from . import views

# url patterns list:
# currently contains index, results, and logout page
urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url('results', views.results, name = 'results'), # create url path to results page
  url(r'^logout/$', views.logout, name='logout') # creatue url path to logout page
]