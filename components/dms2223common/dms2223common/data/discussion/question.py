

from datetime import datetime
from dms2223common.data.discussion.answer import Answer


class Question():

    def __init__(self, autor, title, texto):
        self.autor = autor
        self.texto = texto
        self.tiempo = datetime.now()
        self.visible = True
        self.title = title
        self.respuestas = list()

    def addAnswer(self, child: Answer):
        self.respuestas.append(child)

    def getAnswers(self):
        return self.respuestas

    def changeVisibility(self):
        self.visible = not self.visible
