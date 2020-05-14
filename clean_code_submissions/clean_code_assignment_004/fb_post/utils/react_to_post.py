from fb_post.models import Reaction
from .validators import (is_valid_user_id,
                         is_valid_post_id,
                         is_valid_reaction_type
                        )
from .react_to_comment import update_or_delete_reaction


def react_to_post(user_id, post_id, reaction_type):

    user = is_valid_user_id(user_id)
    post = is_valid_post_id(post_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction_object = Reaction.objects.get(
            reacted_by_id=user_id, post_id=post_id
            )
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            post=post, reaction=reaction_type, reacted_by=user
            )
        return

    update_or_delete_reaction(reaction_object, reaction_type)
