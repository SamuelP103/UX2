from django.urls import path  
# connects the setting for routing
from .views import test_view, about_view
# connects views and the function

urlpatterns = [
    
    #the name for the page then the view and then the name for it
    # the name is useful to call the url pattern ie on the html there is 
    # {%url 'test' %}
    path('testing', test_view, name="test"),
    
    path('', test_view, name="about"),
    
]


