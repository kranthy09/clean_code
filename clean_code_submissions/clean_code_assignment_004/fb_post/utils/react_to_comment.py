from fb_post.models import Reaction
from .validators import (is_valid_user_id, is_valid_comment_id,
                         is_valid_reaction_type
                        )


def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user_id(user_id)
    is_valid_comment_id(comment_id)
    is_valid_reaction_type(reaction_type)

    try:
        reaction_object = Reaction.objects.get(
            reacted_by_id=user_id,
            comment_id=comment_id
            )
    except Reaction.DoesNotExist:
        Reaction.objects.create(
            reacted_by_id=user_id, comment_id=comment_id,
            reaction=reaction_type
            )
        return
    update_or_delete_reaction(reaction_object, reaction_type)


def update_or_delete_reaction(reaction_object, reaction_type):
    is_both_reactions_are_same = reaction_object.reaction == reaction_type

    if is_both_reactions_are_same:
        reaction_object.delete()
    else:
        reaction_object.reaction = reaction_type
        reaction_object.save()
