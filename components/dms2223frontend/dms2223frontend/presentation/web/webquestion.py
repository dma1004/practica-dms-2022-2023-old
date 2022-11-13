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
        """ Gets the list of questions from the backend service.

        Args:
            - backend_service (BackendService): The backend service.

        Returns:
            - List: A list of question data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.list_questions(session.get('token'))
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []

    @staticmethod
    def get_question(backend_service: BackendService, qid: int):
        """ Gets a question from the backend service.

        Args:
            - backend_service (BackendService): The backend service.
            - qid (int): Question ID

        Returns:
            - Question: Dictionary with question data
        """
        response: ResponseData = backend_service.get_question(session.get('token'), qid)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), dict):
            return response.get_content()
        return {}

    @staticmethod
    def get_answers_of_question(backend_service: BackendService, qid: int):
        """ Gets the list of answers of question from the backend service.

        Args:
            - backend_service (BackendService): The backend service.
            - qid (int): Question ID

        Returns:
            - List: A list of answers of question data dictionaries (the list may be empty)
        """
        response: ResponseData = backend_service.get_answers_of_question(session.get('token'), qid)
        WebUtils.flash_response_messages(response)
        if response.get_content() is not None and isinstance(response.get_content(), list):
            return list(response.get_content())
        return []
