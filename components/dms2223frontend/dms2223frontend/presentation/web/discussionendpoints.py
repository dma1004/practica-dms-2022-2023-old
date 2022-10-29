""" DiscussionEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
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

        questions = [Question("Arturo", "¿Aprobamos?", "Buenas tardes"),
                     Question("Asterix", "¿Suspendemos?", "Buenas noches")]
        questions[0].addChild(Answer("Obelix", "Hola"))
        questions[1].addChild(Answer("Pedro", "Adiós"))
        questions[0].getChilds()[0].addChild(Comment("Ángel", "Te equivocas", Feedback.NEGATIVE))

        return render_template('discussion.html', name=name, roles=session['roles'], questions=questions)
