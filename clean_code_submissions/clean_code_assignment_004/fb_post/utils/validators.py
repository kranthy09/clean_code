from fb_post.models import User, Post, Comment
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostContent,
                                InvalidPostException,
                                InvalidCommentException,
                                InvalidCommentContent,
                                InvalidReactionTypeException,
                                InvalidReplyContent,
                                UserCannotDeletePostException
                                )
from fb_post.constants import ReactionChoice


def is_valid_user_id(user_id):

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise InvalidUserException

    return user


def is_valid_post_content(post_content):
    is_invalid_post_content = not post_content
    if is_invalid_post_content:
        raise InvalidPostContent


def is_valid_comment_content(comment_content):
    is_invalid_comment_content = not comment_content
    if is_invalid_comment_content:
        raise InvalidCommentContent


def is_valid_post_id(post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException

    return post

def is_valid_comment_id(comment_id):

    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise InvalidCommentException

    return comment

def is_valid_reply_content(reply_content):
    is_invalid_reply_content = not reply_content

    if is_invalid_reply_content:
        raise InvalidReplyContent


def is_valid_reaction_type(reaction_type):
    is_reaction_type_not_in_reaction_choices = \
        reaction_type not in ReactionChoice.values
    if is_reaction_type_not_in_reaction_choices:
        raise InvalidReactionTypeException


def is_user_is_creator_of_post(user_id, post_id):

    post_object = Post.objects.get(id=post_id)

    is_both_user_id_are_not_same = not post_object.posted_by.id == user_id

    if is_both_user_id_are_not_same:
        raise UserCannotDeletePostException
