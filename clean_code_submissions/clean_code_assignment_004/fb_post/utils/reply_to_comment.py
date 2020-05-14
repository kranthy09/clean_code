from fb_post.models import Comment
from .validators import (is_valid_user_id,
                         is_valid_comment_id,
                         is_valid_reply_content
                        )


def reply_to_comment(user_id, comment_id, reply_content):

    user = is_valid_user_id(user_id)
    comment = is_valid_comment_id(comment_id)
    is_valid_reply_content(reply_content)

    post_of_comment = comment.post
    comment = Comment.objects.create(
        content=reply_content, commented_by=user,
        parent_comment=comment, post=post_of_comment
    )
