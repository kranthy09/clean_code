from django.db.models import Prefetch
from fb_post.models import Post, Comment
from fb_post.constants import time_stamp
from .validators import is_valid_post_id


def get_replies_for_a_comment_in_list(comment, comments_and_replies):
    list_of_replies_to_comment = []
    for each_comment in comments_and_replies:
        is_whether_parent_comment = each_comment.parent_comment == comment
        if is_whether_parent_comment:
            list_of_replies_to_comment.append(each_comment)

    return list_of_replies_to_comment


def get_post(post_id):

    is_valid_post_id(post_id)

    queryset = Comment.objects\
        .select_related('commented_by')\
        .prefetch_related(Prefetch('reaction_set', to_attr='reactions'))

    post = Post.objects.filter(id=post_id)\
        .select_related('posted_by')\
        .prefetch_related(
            Prefetch('reaction_set', to_attr='reactions'),
            Prefetch('comment_set', queryset=queryset, to_attr='comments'))\
        .first()

    query_dict = {}
    comments_list = []
    query_dict = get_post_details_in_dict(post)
    comments_replies_for_a_post = post.comments
    comments_list = get_comments(comments_replies_for_a_post)
    query_dict['comments'] = comments_list

    return query_dict


def get_post_details_in_dict(post):
    query_dict = {
        'post_id': post.id,
        'posted_by': {
            'name': post.posted_by.name,
            'user_id': post.posted_by.id,
            'profile_pic': post.posted_by.profile_pic
        },
        'posted_at': time_stamp(post.posted_at),
        'post_content': post.content,
        'reactions': {
            'count': len(post.reactions),
            'type': [reaction_obj.reaction for reaction_obj in post.reactions]
        }
    }
    return query_dict


def get_comments_for_a_post(comments_replies_for_a_post):
    comments = []
    for comment in comments_replies_for_a_post:
        if not comment.parent_comment:
            comments.append(comment)
    return comments


def get_comment_values_in_dict(comment):

    comment_dict = comment_values_with_out_reactions(comment)
    comment_reactions = comment.reactions
    is_reactions = comment_reactions
    if is_reactions:
        reactions\
            = [reaction_obj.reaction for reaction_obj in comment_reactions]
        reactions_count = len(comment_reactions)
    else:
        reactions = []
        reactions_count = 0
    comment_dict['reactions'] = {
        'count': reactions_count,
        'type': reactions
    }
    return comment_dict


def get_all_replies_detials_appended_in_list(replies):
    replies_key_list = []
    if replies:
        for reply in replies:
            reply_dict = get_comment_values_in_dict(reply)
            replies_key_list.append(reply_dict)
    return replies_key_list


def get_all_comments_details_appended_in_list(comments,
                                              comments_replies_for_a_post
                                             ):
    all_comments_details_in_list = []
    for comment in comments:
        comment_dict = get_comment_values_in_dict(comment)
        replies\
        = get_replies_for_a_comment_in_list(comment,
                                            comments_replies_for_a_post
                                           )
        replies_key_list = get_all_replies_detials_appended_in_list(replies)
        comment_dict['replies_count'] = len(replies)
        comment_dict['replies'] = replies_key_list
        all_comments_details_in_list.append(comment_dict)
    return all_comments_details_in_list


def comment_values_with_out_reactions(comment):

    record = {
        "comment_id": comment.id,
        "commenter": {
            "user_id": comment.commented_by.id,
            "name": comment.commented_by.name,
            "profile_pic": comment.commented_by.profile_pic
        },
        "commented_at": time_stamp(comment.commented_at),
        "comment_content": comment.content,
    }
    return record


def get_comments(comments_replies_for_a_post):
    if comments_replies_for_a_post:
        comments = get_comments_for_a_post(comments_replies_for_a_post)
        comments_list = get_all_comments_details_appended_in_list(
                        comments, comments_replies_for_a_post
        )
    else:
        comments_list = []
    return comments_list
