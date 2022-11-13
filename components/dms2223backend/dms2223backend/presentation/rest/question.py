from http import HTTPStatus

QUESTIONS_DB = {
    0: {
        'qid': 0,
        'title': '¿Aprobamos?',
        'timestamp': 1665574089.0
    },
    1: {
        'qid': 1,
        'title': '¿Suspendemos?',
        'timestamp': 1665574090.0
    }
}


def list_questions():
    return {'questions': list(QUESTIONS_DB.values())}, HTTPStatus.OK
