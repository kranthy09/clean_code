from django.db import models
from .constants import ReactionChoice
# Create your models here.

class User(models.Model):
    
    name = models.CharField(max_length=100)
    profile_pic = models.URLField()


class Post(models.Model):

    content = models.CharField(max_length=1000, null=False)
    posted_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    
    content = models.CharField(max_length=1000)
    commented_at = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True)

class Reaction(models.Model):
    """write enums properly"""
    Reaction_Choice = (
        (ReactionChoice.LOVE.value, ReactionChoice.LOVE.value),
        (ReactionChoice.WOW.value, ReactionChoice.WOW.value),
        (ReactionChoice.HAHA.value, ReactionChoice.HAHA.value),
        (ReactionChoice.LIT.value, ReactionChoice.LIT.value),
        (ReactionChoice.SAD.value, ReactionChoice.SAD.value),
        (ReactionChoice.ANGRY.value, ReactionChoice.ANGRY.value),
        (ReactionChoice.THUMBS_UP.value, ReactionChoice.THUMBS_UP.value),
        (ReactionChoice.THUMBS_DOWN.value, ReactionChoice.THUMBS_DOWN.value)
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,null=True)
    reaction = models.CharField(max_length=100,choices=Reaction_Choice)
    reacted_at = models.DateTimeField(auto_now=True)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)