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

    generado = False
    questions = [Question("Arturo", "¿Aprobamos?", "Buenas tardes"),
                 Question("Asterix", "¿Suspendemos?", "Buenas noches")]

    @staticmethod
    def get_discussion(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not DiscussionEndpoints.generado:
            DiscussionEndpoints.generado = True
            DiscussionEndpoints.questions = [Question("Arturo", "¿Aprobamos?", "Buenas tardes"),
                                             Question("Asterix", "¿Suspendemos?", "Buenas noches")]
            DiscussionEndpoints.questions[0].addAnswer(Answer("Obelix", "Hola"))
            DiscussionEndpoints.questions[1].addAnswer(Answer("Pedro", "Adiós"))
            DiscussionEndpoints.questions[0].getAnswers()[0].addComment(
                Comment("Ángel", "Te equivocas", Feedback.NEGATIVE))

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        return render_template('discussion.html', name=name, roles=session['roles'],
                               questions=DiscussionEndpoints.questions)

    @staticmethod
    def votes_refresh(object, name, upvote):
        """Refresh the votes of Answers and Comments. One user cannot vote for the same thing (upvote or downvote) twice.

        Args:
            object: Answer or Comment to refresh votes
            name: Of the user
            upvote: True if is an upvote or False otherwise

        """
        if upvote:
            if name not in object.votesupusers:  # Los usuarios solo podrán votar una vez
                object.votes += 1
                object.votesupusers.add(name)
                if name in object.votesdownusers:
                    object.votes += 1
                    object.votesdownusers.remove(name)
            else:
                object.votes -= 1
                object.votesupusers.remove(name)
        else:
            if name not in object.votesdownusers:  # Los usuarios solo podrán votar una vez
                object.votes -= 1
                object.votesdownusers.add(name)
                if name in object.votesupusers:
                    object.votes -= 1
                    object.votesupusers.remove(name)
            else:
                object.votes += 1
                object.votesdownusers.remove(name)


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

        if request.method == 'POST':
            n_question = int(request.form.get('questionnumber'))
        else:
            n_question = int(request.args.get('question'))

        question: Question = DiscussionEndpoints.questions[n_question]
        redirect_to: str = str(request.args.get(
            'redirect_to', default='/discussion'))

        if request.method == 'POST':
            n_answer = int(request.form.get('answernumber'))
            answer = question.getAnswers()[n_answer]
            if request.form.get('action') == 'UP':
                if request.form.get('type') == 'voteanswer':  # Vote Answer
                    DiscussionEndpoints.votes_refresh(answer, name, True)
                else:  # Vote Comment
                    n_comment = int(request.form.get('commentnumber'))
                    comment = answer.getComments()[n_comment]
                    DiscussionEndpoints.votes_refresh(comment, name, True)
            elif request.form.get('action') == 'DOWN':
                if request.form.get('type') == 'voteanswer':  # Vote Answer
                    DiscussionEndpoints.votes_refresh(answer, name, False)
                else:  # Vote Comment
                    n_comment = int(request.form.get('commentnumber'))
                    comment = answer.getComments()[n_comment]
                    DiscussionEndpoints.votes_refresh(comment, name, False)

        return render_template('question.html', name=name, roles=session['roles'],
                               question=question,
                               n_question=n_question,
                               redirect_to=redirect_to
                               )
