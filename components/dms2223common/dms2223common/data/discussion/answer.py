from datetime import datetime

from dms2223common.data.discussion.comment import Comment

class Answer:

    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.tiempo = datetime.now()
        self.visible = True
        self.votes = 0
        self.comentarios = list()
        self.votesupusers = set()
        self.votesdownusers = set()

    def voteUp(self):
        self.votes += 1

    def voteDown(self):
        self.votes -= 1
    
    def addComment(self, comment: Comment):
        self.comentarios.append(comment)

    def getComments(self):
        return self.comentarios

    def changeVisibility(self):
        self.visible = not self.visible