from django.contrib import admin
from .models import Post

# to see posts in admin panel we have to register
admin.site.register(Post)
