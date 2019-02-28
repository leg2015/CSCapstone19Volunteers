from django.conf.urls import url
from . import views

# url patterns list:
# currently contains index
urlpatterns = [
  url(r'^$',views.index,name = 'index')
  ]