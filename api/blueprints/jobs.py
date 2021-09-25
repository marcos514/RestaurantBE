import json
import logging

from flask import Blueprint, abort, request, make_response, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from models.job import Job
from serializers.jobs import JobSchema


jobs = Blueprint('jobs', __name__)


@jobs.route('/jobs', methods=['GET'])
def get_jobs():
    # Get and return all the jobs I had
    try:
        jobs = Job.get_all()
        jobs_dump = JobSchema(many=True).dump(jobs)
        return make_response(jsonify(jobs_dump))
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)


@jobs.route('/job', methods=['POST'])
def create_job():
    try:
        job_data = request.json
        job_load = JobSchema().load(job_data)
        job = Job(**job_load)
        job.save()
        job_dump = JobSchema().dump(job)
        return make_response(jsonify(job_dump), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 500)
    except SQLAlchemyError as err:
        logging.error('Error in Job creation: {}'.format(list(err.args)))
        return make_response(jsonify({
            'Error Message': 'There was an error, we coudn\'t create the Job'
        }), 500)
