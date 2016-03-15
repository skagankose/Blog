from django.db import models

# Import time
from django.utils import timezone

class Category(models.Model):

    text = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        try:
            Category.objects.get(text=self.text)
        except:
            super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

# Post model
class Post(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='img/', blank=True)
    item_position = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, related_name='posts')
    edited = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        super(Post, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(pk=self.pk)
            if this.thumbnail != self.thumbnail:
                this.thumbnail.delete(save=False)
        except: pass
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return str(self.pk) + '-' +  self.title

# GeneralFile model
class GeneralFile(models.Model):
	post = models.ForeignKey(Post, related_name='general_files')
	position = models.IntegerField(default=9999)
	file_item = models.FileField(upload_to='file/', blank=True)
	image = models.BooleanField(default=False)
	video = models.BooleanField(default=False)
	other = models.BooleanField(default=False)
	edited = models.BooleanField(default=False)


	def delete(self, *args, **kwargs):
	    self.file_item.delete()
	    super(GeneralFile, self).delete(*args, **kwargs)

	def save(self, *args, **kwargs):
	    try:
	        this = GeneralFile.objects.get(pk=self.pk)
	        if this.file_item != self.file_item:
	            this.file_item.delete(save=False)
	    except: pass
	    super(GeneralFile, self).save(*args, **kwargs)

	class Meta:
	    ordering = ['position']

	def __str__(self):
	    return 'file-' + str(self.pk)

# GeneralText model
class GeneralText(models.Model):

    post = models.ForeignKey(Post, related_name='general_texts')
    position = models.IntegerField(default=9999)
    text = models.TextField()
    paragraph = models.BooleanField(default=False)
    heading = models.BooleanField(default=False)
    subheading = models.BooleanField(default=False)
    subsubheading = models.BooleanField(default=False)
    list_item = models.BooleanField(default=False)
    inline_block = models.BooleanField(default=False)
    code = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    link = models.BooleanField(default=False)
    youtube = models.BooleanField(default=False)
    is_safe = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.post.title + '-' + str(self.pk)
