""" WebUser class module.
"""

from typing import Dict, List, Optional
from flask import session
from dms2223common.data.rest import ResponseData
from dms2223frontend.data.rest.backendservice import BackendService
from .webutils import WebUtils


class WebQuestion():
    """ Monostate class responsible of the question operation utilities.
    """

    @staticmethod
    def list_questions(backend_service: BackendService) -> List:
        """ Gets the list of users from the authentication service.

        Args:
            - backend_service (BackendService): The authentication service.

        Returns:
            - List: A list of user data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_questions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []
