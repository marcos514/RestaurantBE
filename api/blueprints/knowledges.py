import json
import logging

from flask import Blueprint, abort, request, make_response, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from models.knowledge import Knowledge
from serializers.knowledges import KnowledgeSchema


knowledges = Blueprint('knowledges', __name__)


@knowledges.route('/knowledges', methods=['GET'])
def get_knowledges():
    # Get and return all the knowledges I had
    try:
        knowledges = Knowledge.get_all()
        knowledges_dump = KnowledgeSchema(many=True).dump(knowledges)
        return make_response(jsonify(knowledges_dump))
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)


@knowledges.route('/knowledge', methods=['POST'])
def create_knowledge():
    try:
        knowledge_data = request.json
        knowledge_load = KnowledgeSchema().load(knowledge_data)
        knowledge = Knowledge(**knowledge_load)
        knowledge.save()
        knowledge_dump = KnowledgeSchema().dump(knowledge)
        return make_response(jsonify(knowledge_dump), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)
    except SQLAlchemyError as err:
        logging.error('Error in Knowledge creation: {}'.format(list(err.args)))
        return make_response(jsonify({
            'Error Message': 'There was an error, we coudn\'t create the new Knowledge'
        }), 500)
