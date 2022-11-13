""" DiscussionEndpoints class module.
"""

from typing import Text, Union

from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response

from dms2223common.data import Role
from dms2223frontend.data.rest.backendservice import BackendService
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
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']

        return render_template('questions.html', name=name, roles=session['roles'],
                               questions=WebQuestion.list_questions(backend_service)
                               )
