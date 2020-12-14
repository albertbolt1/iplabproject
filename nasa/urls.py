
from django.urls import path
from . import views
app_name = 'nasa'
urlpatterns = [
    path('',views.home,name='landingpage'),
    path('options',views.optionspage,name='optionspage'),
    path('first',views.pictureoftheday,name='pictureoftheday'),
    path('second',views.nearearthobjects,name='nearearthobjects'),
    path('third',views.allmeteorlandings,name='allmeteorlandings'),
    path('fourth',views.getlocnearmeteor,name='getlocnearmeteor'),
    path('fifth',views.marsroverpics,name='marsroverpics'),
    path('nearearthobjectssendinfo',views.nearearthobjectsdisplay,name='nearearthobjectsdisplay'),
    path('getlocationgivedata',views.getlocationgivedata,name='getlocationgivedata'),
    path('roverpicsdisplay',views.getroverpics,name='roverpicsdisplay'),
    path('pollutionmap',views.pollutionmap,name='lightpollutionmap')
]
