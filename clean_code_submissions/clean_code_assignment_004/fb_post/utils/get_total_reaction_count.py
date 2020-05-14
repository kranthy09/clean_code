from django.db.models import Count
from fb_post.models import Reaction


def get_total_reaction_count():

    total_reaction_count = Reaction.objects\
        .aggregate(count=Count('reaction'))

    return total_reaction_count
