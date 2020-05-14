from fb_post.models import Comment
from .validators import (is_valid_user_id, is_valid_post_id,
                         is_valid_comment_content
                        )


def create_comment(user_id, post_id, comment_content):

    user = is_valid_user_id(user_id)
    post = is_valid_post_id(post_id)
    is_valid_comment_content(comment_content)

    comment = Comment.objects.create(
        commented_by=user, post=post, content=comment_content
    )
    return comment.id
