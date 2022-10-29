from dms2223common.data.discussion.discussion_component import DiscussionComponent
from enum import Enum


class Feedback(Enum):
    """ Enumeration with the feedback.
    """
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3


class Comment(DiscussionComponent):

    def __init__(self, autor, texto, feedback: Feedback):
        super().__init__(autor, texto)
        self.feedback = feedback
        self.votes = 0

    def voteUp(self):
        self.votes += 1

    def voteDown(self):
        self.votes -= 1
