""" DiscussionEndpoints class module.
"""

from typing import Text, Union

from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response

from dms2223common.data import Role
from dms2223frontend.data.rest.backendservice import BackendService
from .webauth import WebAuth
from .webquestion import WebQuestion


class QuestionEndpoints():
    """ Monostate class responsible of handling the question web endpoint requests.
    """


    @staticmethod
    def get_questions(backend_service: BackendService) -> Union[Response, Text]:
        """ Handles the GET requests to a particular question endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(backend_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']

        return render_template('question.html', name=name, roles=session['roles'],
                               question=question,
                               n_question=n_question,
                               redirect_to=redirect_to
                               )
