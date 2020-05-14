from fb_post.models import Reaction
from .validators import is_valid_post_id


def get_reactions_to_post(post_id):

    is_valid_post_id(post_id)

    reaction_objects = Reaction.objects\
        .filter(post_id=post_id)\
        .select_related('reacted_by')

    list_of_reactions_for_a_post = []
    for reaction_obj in reaction_objects:

        list_of_reactions_for_a_post\
            .append(get_reaction_object_with_attributes_in_dict(reaction_obj))

    return list_of_reactions_for_a_post

def get_reaction_object_with_attributes_in_dict(reaction_obj):

    record = {
                "user_id" : reaction_obj.reacted_by.id,
                "name" : reaction_obj.reacted_by.name,
                "profile_pic" : reaction_obj.reacted_by.profile_pic,
                "reaction" : reaction_obj.reaction
    }

    return record
