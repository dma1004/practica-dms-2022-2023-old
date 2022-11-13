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

QUESTIONSFULL_DB = {
    0: {
        'qid': 0,
        'title': '¿Aprobamos?',
        'body': 'Hay que trabajar mucho',
        'owner': {'username': 'Arturo'},
        'timestamp': 1665574089.0
    },
    1: {
        'qid': 1,
        'title': '¿Suspendemos?',
        'body': 'Si trabajamos poco',
        'owner': {'username': 'Pedro'},
        'timestamp': 1665574090.0
    }
}

ANSWERS_DB = {
    0: {
        'id': 0,
        'qid': 0,
        'timestamp': 1665575089,
        'body': 'I would suggest four members.',
        'owner': {'username': 'user3'},
        'votes': 4,
        'user_votes': {'user3': True},
        'comments': [
            {
                'aid': 0,
                'body': 'Evaluation criteria may be relaxed due to the tight number of members',
                'id': 1,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'POSITIVE',
                'timestamp': 1665575389,
                'user_votes': {
                    'user5': True,
                    'user6': True
                },
                'votes': 2
            },
            {
                'aid': 0,
                'body': 'Enough to distribute the workload equitatively',
                'id': 0,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'POSITIVE',
                'timestamp': 1665575289,
                'user_votes': {
                    'user6': True
                },
                'votes': 1
            },
            {
                'aid': 0,
                'body': 'The deadline may be too close for the workload and a group this \'small\'',
                'id': 2,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'NEGATIVE',
                'timestamp': 1665577389,
                'user_votes': [],
                'votes': 0
            }
        ]
    },
    1: {
        'id': 0,
        'qid': 1,
        'timestamp': 1665575089,
        'body': 'I would suggest four members.',
        'owner': {'username': 'user3'},
        'votes': 4,
        'user_votes': {'user3': True},
        'comments': [
            {
                'aid': 0,
                'body': 'Evaluation criteria may be relaxed due to the tight number of members',
                'id': 1,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'POSITIVE',
                'timestamp': 1665575389,
                'user_votes': {
                    'user5': True,
                    'user6': True
                },
                'votes': 2
            },
            {
                'aid': 0,
                'body': 'Enough to distribute the workload equitatively',
                'id': 0,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'POSITIVE',
                'timestamp': 1665575289,
                'user_votes': {
                    'user6': True
                },
                'votes': 1
            },
            {
                'aid': 0,
                'body': 'The deadline may be too close for the workload and a group this \'small\'',
                'id': 2,
                'owner': {
                    'username': 'user4'
                },
                'sentiment': 'NEGATIVE',
                'timestamp': 1665577389,
                'user_votes': [],
                'votes': 0
            }
        ]
    }
}


def list_questions():
    return list(QUESTIONS_DB.values()), HTTPStatus.OK


def get_question(qid):
    return QUESTIONSFULL_DB[qid], HTTPStatus.OK


def get_answers(qid):
    answers = list()
    for a in ANSWERS_DB.values():
        if a['qid'] == qid:
            answers.append(a)
    return answers, HTTPStatus.OK
