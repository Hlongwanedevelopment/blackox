from django.urls import path 
from website import views 
from website.views import (
    Blog,
    Blogdetail,
    CattleDetail
)

app_name = 'website'
urlpatterns = [
    path("", views.landing, name='landing'),
    path("Our-Breed/", views.ourbreed, name="ourbreed"),
    path("About-BlackOX/", views.aboutfarm, name="about"),
    path("Contact-BlackOX/", views.contact, name="contact"),
    path("Careers/", views.careers, name="careers"),
    path("FAQs/", views.FAQ, name="faqs"),
    path("news-feed/", Blog.as_view(), name="blog"),
    path("article/<int:pk>", Blogdetail.as_view(), name="article-detail"),
    path("cattle/<int:pk>/", CattleDetail.as_view(), name="cattledetail")
]
