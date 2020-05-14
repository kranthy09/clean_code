from django.db.models import Prefetch
from fb_post.models import Post, Comment
from .validators import is_valid_user_id
from .get_post import (get_post_details_in_dict,
                       get_comments
                      )


def get_user_posts(user_id):

    is_valid_user_id(user_id)
    queryset = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related(Prefetch('reaction_set', to_attr='reactions'))

    posts = Post.objects.filter(posted_by=user_id)\
        .select_related('posted_by')\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='reactions'),
            Prefetch('comment_set', queryset=queryset, to_attr='comments'))
    result = []
    for post in posts:
        query_dict = {}
        query_dict = get_post_details_in_dict(post)
        comments_replies_for_a_post = post.comments
        comments_list = get_comments(comments_replies_for_a_post)
        query_dict['comments'] = comments_list
        result.append(query_dict)
    return result
