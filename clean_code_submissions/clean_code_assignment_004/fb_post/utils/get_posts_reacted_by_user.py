from fb_post.models import Reaction
from .validators import is_valid_user_id


def get_posts_reacted_by_user(user_id):

    is_valid_user_id(user_id)
    post_ids_reacted_by_user = list(
        Reaction.objects.filter(reacted_by=user_id, post_id__isnull=False)\
        .values_list('post_id', flat=True)
    )

    return post_ids_reacted_by_user
