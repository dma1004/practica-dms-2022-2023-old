from datetime import datetime


class DiscussionComponent:

    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.tiempo = datetime.now()
        self.visible = True

    def changeVisibility(self):
        self.visible = not self.visible
