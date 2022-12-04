from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    author_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.author_rating

    def update_rating(self):
        update_post_rating = Post.objects.all().aggregate(s=Sum('post_rating')*3)
        update_comment_rating = Comment.objects.all().aggregate(s=Sum('comment_rating'))


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    ARTICLE = 'A'
    NEWS = 'N'
    CHOICE = [
        ('A', 'article'),
        ('N', 'news'),
    ]
    choice = models.CharField(
        max_length=50,
        choices=CHOICE,
        default=NEWS
    )
    data_time = models.DateTimeField(auto_now_add=True)
    post_title = models.TextField()
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    author_relation = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_relation = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return self.post_text[:125] + "..."

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()


class PostCategory(models.Model):
    post_relation = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_relation = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    post_relation = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_relation = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.comment_rating += 1

    def dislike(self):
        self.comment_rating -= 1



