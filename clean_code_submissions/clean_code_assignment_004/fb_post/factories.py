import factory.fuzzy
from .models import User, Reaction, Post, Comment
import datetime
import string

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
    name = factory.Sequence(lambda n: 'user%d' % n)
    profile_pic = factory.LazyAttribute(lambda obj: '%s.com' % obj.name)

class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post
    content = factory.fuzzy.FuzzyText(length=20, chars=string.ascii_letters)
    posted_at = factory.LazyFunction(datetime.datetime.now)
    posted_by = factory.Iterator(User.objects.all())

class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    post = factory.Iterator(Post.objects.all())
    commented_by = factory.Iterator(User.objects.all())
    content = factory.fuzzy.FuzzyText(length=5, chars=string.ascii_letters)
    commented_at = factory.LazyFunction(datetime.datetime.now)
    parent_comment = None

class ReplyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    commented_by = factory.Iterator(User.objects.all())
    content = factory.fuzzy.FuzzyText(length=5, chars=string.ascii_letters)
    commented_at = factory.LazyFunction(datetime.datetime.now)
    parent_comment = factory.Iterator(Comment.objects.all())

class ReactionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Reaction

    post = factory.Iterator(Post.objects.all())
    comment = factory.Iterator(Comment.objects.all())
    reaction = factory.fuzzy.FuzzyChoice(Reaction.Reaction_Choice, getter=lambda c : c[0])
    reacted_at = factory.LazyFunction(datetime.datetime.now)
    reacted_by = factory.Iterator(User.objects.all())