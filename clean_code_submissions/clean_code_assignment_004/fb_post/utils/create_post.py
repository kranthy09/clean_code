from fb_post.models import Post
from .validators import is_valid_user_id, is_valid_post_content


def create_post(user_id, post_content):
    user = is_valid_user_id(user_id)
    is_valid_post_content(post_content)
    post = Post.objects.create(content=post_content, posted_by=user)
    return post.id
