from flask import Flask, request, g
from db.db import query_db
from utils import zip_rows
from collections import Counter

app = Flask(__name__)


@app.route('/')
def up_and_running():
    return {
        'data': "I'm alive!",
        'error': None
    }


@app.route('/variables/<string:variable_id>', methods=['GET'])
def get_variable(variable_id):
    if request.method == 'GET':
        variable_data = query_db('''
            SELECT *
            FROM variable_taxonomy
            WHERE variable_uuid == ?
        ''', [variable_id])

        if len(variable_data) > 0:

            variable_dict = zip_rows(variable_data)

            return {
                'data': {
                    'label': variable_dict[0]['variable_label'],
                    'options': [
                        {
                            'code': element['answer_code'],
                            'label': element['answer_label'],
                            'option': element['answer_option']
                        }
                        for element in variable_dict],
                    'question': variable_dict[0]['variable_question'],
                    'type': variable_dict[0]['variable_type'],
                    'uuid': variable_dict[0]['variable_uuid'],
                },
                'error': None
            }

        else:
            return {
                'data': None,
                'error': 'No question found with the provided variable_id'
            }

    else:
        return {
            'data': None,
            'error': 'Invalid HTTP method'
        }


@app.route('/variables/<string:variable_id>/counts', methods=['GET'])
def count_answers(variable_id):
    if request.method == 'GET':
        answers_data = query_db('''
            SELECT *
            FROM answers
            WHERE variable_uuid == ?
        ''', [variable_id])

        if len(answers_data) > 0:

            answers_dict = zip_rows(answers_data)

            return {
                'data': Counter([answer['value'] for answer in answers_dict]),
                'error': None
            }

        else:
            return {
                'data': None,
                'error': 'No answers found with the variable_id provided'
            }

    else:
        return {
            'data': None,
            'error': 'Invalid HTTP method'
        }


@app.teardown_appcontext
def close_connection(exception):
    print('Closing database connection...')
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        print('Database closed successfully ✅')
