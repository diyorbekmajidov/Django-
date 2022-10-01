from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('index/', views.index),
]
# def home(request):
#     a = request.GET.get("a",0)
#     b =request.GET.get("b",0)
#     print(int(a)+int(b))
#     r = JsonResponse({"message":'Hello Word',"sum":int(a)+int(b)})
#     return r 
