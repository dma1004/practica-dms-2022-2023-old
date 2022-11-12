from enum import Enum
from datetime import datetime


class Feedback(Enum):
    """ Enumeration with the feedback.
    """
    POSITIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3


class Comment():

    def __init__(self, autor, texto, feedback: Feedback):
        self.autor = autor
        self.texto = texto
        self.tiempo = datetime.now()
        self.visible = True
        self.feedback = feedback
        self.votes = 0
        self.votesupusers = set()
        self.votesdownusers = set()

    def voteUp(self):
        self.votes += 1

    def voteDown(self):
        self.votes -= 1
    
    def changeVisibility(self):
        self.visible = not self.visible
