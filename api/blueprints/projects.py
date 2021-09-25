import json
import logging

from flask import Blueprint, abort, request, make_response, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from models.project import Project
from serializers.projects import ProjectSchema


projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=['GET'])
def get_projects():
    # Get and return all the projects I had
    try:
        project = Project.get_all()
        project_dump = ProjectSchema(many=True).dump(project)
        return make_response(jsonify(project_dump))
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)


@projects.route('/project', methods=['POST'])
def create_project():
    try:
        project_data = request.json
        project_load = ProjectSchema().load(project_data)
        project = Project(**project_load)
        project.save()
        project_dump = ProjectSchema().dump(project)
        return make_response(jsonify(project_dump), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)
    except SQLAlchemyError as err:
        logging.error('Error in Project creation: {}'.format(list(err.args)))
        return make_response(jsonify({
            'Error Message': 'There was an error, we coudn\'t create the new Project'
        }), 500)
