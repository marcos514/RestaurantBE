"""first migration

Revision ID: 3b5b0d664a85
Revises: 
Create Date: 2020-04-23 22:23:17.804425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b5b0d664a85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('company_name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(500), nullable=False),
        sa.Column('date_from', sa.String(50), nullable=False),
        sa.Column('date_to', sa.String(50), nullable=True),
        sa.Column('job_type', sa.String(50), nullable=False)
    )

    op.create_table(
        'knowledges',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('parent_knowledge', sa.Integer, sa.ForeignKey("knowledges.id"), nullable=True),
        sa.CheckConstraint('level >= 0', name='level_min'),
        sa.CheckConstraint('level <= 100', name='level_max')
    )

    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(500), nullable=False),
        sa.Column('date_started', sa.String(50), nullable=False),
        sa.Column('date_finished', sa.String(50), nullable=True),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('percentage_done', sa.Integer, nullable=False, default=0),
        sa.CheckConstraint('percentage_done >=0', name='percentage_done_min'),
        sa.CheckConstraint('percentage_done <=100', name='percentage_done_max')
    )

    op.create_check_constraint(
        "status_list",
        "projects",
        "status in ('Started','Stoped','Finished','Blocked','Future')"
        )

    op.create_table(
        'project_knowledges',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('knowledge_id', sa.Integer, sa.ForeignKey('knowledges.id')),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id'))
    )


def downgrade():
    op.drop_table('jobs')
    op.drop_table('knowledges')
    op.drop_table('projects')
    op.drop_table('project_knowledges')
