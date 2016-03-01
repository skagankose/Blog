# Core
from django import forms

# Import time
from django.utils import timezone

# Ours'
from .models import Post, GeneralText, GeneralFile, Category

# Create Post
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('thumbnail', 'title', 'description', 'category',)

# Create GeneralText
class GeneralTextForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style':'resize:vertical;'}))
    class Meta:
        model = GeneralText
        fields = ('text',)

# Create GeneralFile
class GeneralFileForm(forms.ModelForm):
    class Meta:
        model = GeneralFile
        fields = ('file_item',)

# Create Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('text',)

# Edit GeneralText
class EditGeneralTextForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,'style':'resize:vertical;'}))
    class Meta:
        model = GeneralText
        fields = ('text', 'position',)

# Edit GeneralFile
class EditGeneralFileForm(forms.ModelForm):
    class Meta:
        model = GeneralFile
        fields = ('position',)

# Edit Post
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('thumbnail', 'title', 'description', 'category', 'item_position')