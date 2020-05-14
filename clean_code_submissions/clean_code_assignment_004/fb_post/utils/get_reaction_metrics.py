from django.db.models import Count
from fb_post.models import Reaction
from .validators import is_valid_post_id

def get_reaction_metrics(post_id):

    is_valid_post_id(post_id)

    reaction_metrics = Reaction.objects\
        .filter(post_id=post_id)\
        .values_list('reaction')\
        .annotate(count=Count('reaction'))

    return dict(reaction_metrics)
