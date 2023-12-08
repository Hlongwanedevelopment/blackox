from django.contrib import admin
from website.models import (
    Breed, 
    Cattle,
    Sheep,
    Contact,
    Post,
    JobPost,
    FarmOperation
)
# Register your models here.

admin.site.register(Breed)
admin.site.register(Cattle)
admin.site.register(Sheep)
admin.site.register(Contact)
admin.site.register(JobPost)
admin.site.register(Post)
admin.site.register(FarmOperation)