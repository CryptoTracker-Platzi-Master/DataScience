from django.urls import path
from algorithms.views import home, Compound, Nominal

urlpatterns = [    
    path('', home),
    path('compound/', Compound.as_view()),
    path('nominal/', Nominal.as_view()),
]
