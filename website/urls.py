from django.urls import path 
from website import views 
from website.views import (
    Blog,
    Blogdetail,
)

app_name = 'website'
urlpatterns = [
    path("icd", views.indcnt, name=""),
    path("", views.landing, name='landing'),
    path("Farm-operations/", views.farmoperations, name="farmoperations"),
    path("farmoperation/<int:pk>/", views.farmoperationdetail, name="operationdetail"),
    path("About-BlackOX/", views.aboutfarm, name="about"),
    path("Contact-BlackOX/", views.contact, name="contact"),
    path("Careers/", views.careers, name="careers"),
    path("job-post/<int:pk>/", views.careerdetail, name="careerdetail"),
    path("apply-to-post/<int:pk>/", views.applytopost, name="applytopost"),
    path("FAQs/", views.FAQ, name="faqs"),
    path("ourfarms/", views.ourfarms, name="ourfarms"),
    path("news-feed/", Blog.as_view(), name="blog"),
    path("article/<int:pk>", Blogdetail.as_view(), name="article-detail"),
]
