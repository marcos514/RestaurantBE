from marshmallow import Schema, fields


class JobSchema(Schema):
    id = fields.Int(required=False)
    company_name = fields.Str(required=True)
    description = fields.Str(required=True)
    date_from = fields.Str(required=True)
    date_to = fields.Str(required=False)
    job_type = fields.Str(required=True)

