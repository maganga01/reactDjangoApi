from django.urls import path
from. views import ReactView

app_name = "core"
from .views import ReactView

urlpatterns = [
     path('well/', ReactView.as_view(), name="wellcome"),
]

