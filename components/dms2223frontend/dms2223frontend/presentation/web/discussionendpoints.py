""" DiscussionEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223common.data.discussion.answer import Answer
from dms2223common.data.discussion.comment import Comment, Feedback
from dms2223common.data.discussion.question import Question
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth


class DiscussionEndpoints():
    """ Monostate class responsible of handling the discussion web endpoint requests.
    """

    @staticmethod
    def preguntas() -> [Question]:
        questions = [Question("Arturo", "¿Aprobamos?", "Buenas tardes"),
                     Question("Asterix", "¿Suspendemos?", "Buenas noches")]
        questions[0].addChild(Answer("Obelix", "Hola"))
        questions[1].addChild(Answer("Pedro", "Adiós"))
        questions[0].getChilds()[0].addChild(Comment("Ángel", "Te equivocas", Feedback.NEGATIVE))

        return questions


    @staticmethod
    def get_discussion(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('discussion.html', name=name, roles=session['roles'],
                               questions=DiscussionEndpoints.preguntas())

    @staticmethod
    def get_question(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to a particular question endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        question: Question = DiscussionEndpoints.preguntas()[int(request.args.get('question'))]
        redirect_to: str = str(request.args.get(
            'redirect_to', default='/discussion'))
        return render_template('question.html', name=name, roles=session['roles'],
                               question=question,
                               redirect_to=redirect_to
                               )
