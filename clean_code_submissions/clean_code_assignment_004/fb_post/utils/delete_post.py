from fb_post.models import Post
from .validators import (is_valid_user_id,
                         is_valid_post_id,
                         is_user_is_creator_of_post)


def delete_post(user_id, post_id):

    is_valid_user_id(user_id)
    is_valid_post_id(post_id)
    is_user_is_creator_of_post(user_id, post_id)
    Post.objects.filter(id=post_id).delete()
