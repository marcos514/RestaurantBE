from marshmallow import Schema, fields, validate


class KnowledgeSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str(required=True)
    level = fields.Int(validate=validate.Range(min=0, max=100), required=True)
    parent_knowledge = fields.Int(required=False)
    child_knowledges = fields.List(fields.Nested('KnowledgeSchema', only=('name', 'level', 'id')))

