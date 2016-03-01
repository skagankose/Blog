from django.contrib import admin

# Ours'
from .models import Post, GeneralText, GeneralFile, Category

# Register our models
admin.site.register(Post)
admin.site.register(GeneralText)
admin.site.register(GeneralFile)
admin.site.register(Category)

