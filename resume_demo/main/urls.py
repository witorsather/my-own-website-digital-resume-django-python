# we wired this main app into our url, so everything that appears here are urls specific to main
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # localhost post 8000
    # my home page
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog")
]