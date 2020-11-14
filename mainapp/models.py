from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

#blog post model and attributes
class Post(models.Model):
    title = models.CharField(max_length=200)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True,null=True)
    date_posted = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} - {self.author}"
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk':self.pk})
    class Meta:
        ordering = ('-date_posted',)    

#model blog comment
class Comment(models.Model):
    post =models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Comment By {}'.format(self.name)

class MarketPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_item = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    description =models.TextField(max_length=500,default="About my sales")
    image = models.FileField(upload_to="marketplace/")
    contact = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.type_of_item}-{self.quantity}"
    def get_absolute_url(self):
        return reverse('market_detail', kwargs={'pk':self.pk})


class PostAgriProblem(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Agridoctor/")
    description = models.TextField(max_length=400)
    date_posted = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.author}"
    def get_absolute_url(self):
        return reverse('agridoctor_detail', kwargs={'pk':self.pk})
    class Meta:
        ordering = ('-date_posted',)   

class AgriComment(models.Model):
    post =models.ForeignKey(PostAgriProblem ,on_delete=models.CASCADE,related_name="comments")
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return 'Comment By {}'.format(self.name)


class Test(models.Model):
    test = models.CharField(max_length=200)


     