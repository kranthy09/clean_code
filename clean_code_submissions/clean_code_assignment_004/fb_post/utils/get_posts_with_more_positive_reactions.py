from django.db.models import Prefetch, Q, Count
from fb_post.models import Post


def get_posts_with_more_positive_reactions():

    posts = Post.objects\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='reactions_to_this_post'))\
        .filter(Q(reaction__reaction="HAHA") |
                Q(reaction__reaction="LOVE") |
                Q(reaction__reaction="LIT") |
                Q(reaction__reaction="WOW") |
                Q(reaction__reaction="THUMBS-UP")
                )\
        .annotate(positive_reactions_count=Count('reaction'))
    list_of_post_with_more_postive_reactions = []
    for post in posts:
        post_has_more_postive_reactions\
            = is_post_has_more_positive_reactions(post)
        if post_has_more_postive_reactions:
            list_of_post_with_more_postive_reactions.append(post)
    return list_of_post_with_more_postive_reactions


def is_post_has_more_positive_reactions(post):
    total_reactions = len(post.reactions_to_this_post)
    positive_reactions = post.positive_reactions_count
    check_for_more_positive_reactions\
        = positive_reactions / total_reactions >= 0.50
    return check_for_more_positive_reactions
