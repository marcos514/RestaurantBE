from marshmallow import Schema, fields, validate
from serializers.knowledges import KnowledgeSchema


class ProjectSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    date_started = fields.Str(required=True)
    date_finished = fields.Str(required=False)
    status = fields.Str(required=False)
    percentage_done = fields.Int(required=False)
    knowledges = fields.List(fields.Nested('KnowledgeSchema', only=('name', 'id')))
    knowledges_id = fields.List(fields.Int(required=False))

