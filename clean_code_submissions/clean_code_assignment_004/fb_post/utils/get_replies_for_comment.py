from fb_post.models import Comment
from .get_post import comment_values_with_out_reactions


def get_replies_for_comment(comment_id):

    comments = Comment.objects\
        .filter(parent_comment_id=comment_id)\
        .select_related('commented_by')
    list_of_replies_for_comment = []
    for comment in comments:
        list_of_replies_for_comment\
            .append(comment_values_with_out_reactions(comment))

    return list_of_replies_for_comment
