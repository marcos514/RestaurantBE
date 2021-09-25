import config

from flask import Flask
from flask_cors import CORS, cross_origin

from blueprints import jobs, knowledges, projects

app = Flask(__name__)
CORS(app, resources=r'/*', allow_headers='Content-Type')



app.register_blueprint(jobs.jobs)
app.register_blueprint(projects.projects)
app.register_blueprint(knowledges.knowledges)


if __name__ == '__main__':
    configuration = {
        'host': '0.0.0.0',
        'port': config.FLASK_PORT,
        'debug': config.FLASK_DEBUG
    }
    app.run(**configuration)
