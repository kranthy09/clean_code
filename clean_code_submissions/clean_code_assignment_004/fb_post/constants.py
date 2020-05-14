from django.db import models
from datetime import datetime


class ReactionChoice(models.TextChoices):

    WOW = 'WOW'
    LIT = 'LIT'
    LOVE = 'LOVE'
    HAHA = 'HAHA'
    THUMBS_UP = 'THUMBS-UP'
    THUMBS_DOWN = 'THUMBS-DOWN'
    ANGRY = 'ANGRY'
    SAD = 'SAD'


def time_stamp(date_time):
    created_time = datetime.strftime(date_time, "%Y-%m-%d, %X.%f")
    return created_time