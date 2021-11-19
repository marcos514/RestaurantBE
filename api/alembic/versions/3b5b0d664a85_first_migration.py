"""first migration

Revision ID: 3b5b0d664a85
Revises: 
Create Date: 2020-04-23 22:23:17.804425

"""
from datetime import datetime

from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b5b0d664a85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table(
    #     'jobs',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('company_name', sa.String(50), nullable=False),
    #     sa.Column('description', sa.String(500), nullable=False),
    #     sa.Column('date_from', sa.String(50), nullable=False),
    #     sa.Column('date_to', sa.String(50), nullable=True),
    #     sa.Column('job_type', sa.String(50), nullable=False)
    # )

    # op.create_table(
    #     'knowledges',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('name', sa.String(50), nullable=False, unique=True),
    #     sa.Column('level', sa.Integer, nullable=False),
    #     sa.Column('parent_knowledge', sa.Integer, sa.ForeignKey("knowledges.id"), nullable=True),
    #     sa.CheckConstraint('level >= 0', name='level_min'),
    #     sa.CheckConstraint('level <= 100', name='level_max')
    # )

    # op.create_table(
    #     'projects',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('name', sa.String(50), nullable=False),
    #     sa.Column('description', sa.String(500), nullable=False),
    #     sa.Column('date_started', sa.String(50), nullable=False),
    #     sa.Column('date_finished', sa.String(50), nullable=True),
    #     sa.Column('status', sa.String(50), nullable=False),
    #     sa.Column('percentage_done', sa.Integer, nullable=False, default=0),
    #     sa.CheckConstraint('percentage_done >=0', name='percentage_done_min'),
    #     sa.CheckConstraint('percentage_done <=100', name='percentage_done_max')
    # )

    # op.create_check_constraint(
    #     "status_list",
    #     "projects",
    #     "status in ('Started','Stoped','Finished','Blocked','Future')"
    #     )

    # op.create_table(
    #     'project_knowledges',
    #     sa.Column('id', sa.Integer, primary_key=True),
    #     sa.Column('knowledge_id', sa.Integer, sa.ForeignKey('knowledges.id')),
    #     sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id'))
    # )
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False, unique=True),
        sa.Column('dob', sa.Date(), nullable=False),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('phone_number', sa.String(30), nullable=True),
        sa.CheckConstraint("email ~* '^[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}'", name='email_validator'),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'client',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('rewards_points', sa.Integer, nullable=False, default=0),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address1', sa.String(100), nullable=False),
        sa.Column('address1', sa.String(50), nullable=True),
        sa.Column('city', sa.String(25), nullable=False),
        sa.Column('province', sa.String(25), nullable=False),
        sa.Column('zip', sa.String(10), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'client_address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('is_default', sa.Boolean, nullable=False),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('client.id')),
        sa.Column('address_id', sa.Integer, sa.ForeignKey('address.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'system_access',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'system_panel',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('access_id', sa.Integer, sa.ForeignKey('system_access.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'system_credential',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('credential_name', sa.String(50), nullable=False, unique=True),
        sa.Column('panel_id', sa.Integer, sa.ForeignKey('system_panel.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'job_type',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    #Need to work in working hours
    op.create_table(
        'worker',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('credential_name', sa.String(50), nullable=False, unique=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('job_type_id', sa.Integer, sa.ForeignKey('job_type.id')),
        sa.Column('credential_id', sa.Integer, sa.ForeignKey('system_credential.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'tag',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('description', sa.String(500), nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'product_tag',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tag_id', sa.Integer, sa.ForeignKey('tag.id')),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'product_configurator',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('min_quantity', sa.Integer, nullable=True),
        sa.Column('max_quantity', sa.Integer, nullable=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'extra_product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('price', sa.Float, nullable=True),
        sa.Column('extra_product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('product_configurator_id', sa.Integer, sa.ForeignKey('product_configurator.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'extra_product_type',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('price', sa.Float, nullable=True),
        sa.Column('product_tag_id', sa.Integer, sa.ForeignKey('tag.id')),
        sa.Column('product_configurator_id', sa.Integer, sa.ForeignKey('product_configurator.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'table_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('max_capacity', sa.Integer, nullable=False, default=4),
        sa.Column('code', sa.String(3), nullable=False),
        sa.Column('status_id', sa.Integer, sa.ForeignKey('table_status.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'order',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status_id', sa.Integer, sa.ForeignKey('order_status.id')),
        sa.Column('worker_id', sa.Integer, sa.ForeignKey('worker.id')),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('client.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'order_product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String(25), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('order.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('special_requirement', sa.String(500), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'order_product_extra',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String(25), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('order_product_id', sa.Integer, sa.ForeignKey('order_product.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('special_requirement', sa.String(500), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'order_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('table_id', sa.Integer, sa.ForeignKey('table.id')),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('order.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'discount_code',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Float, nullable=False),
        sa.Column('value_type', sa.String(25), nullable=False),
        sa.Column('code', sa.String(25), nullable=False),
        sa.Column('usage_limits', sa.Integer, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('ends_at', sa.DateTime, nullable=True),
        sa.Column('starts_at', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )


    op.create_table(
        'bill',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String(25), nullable=False),
        sa.Column('subtotal_price', sa.Float, nullable=False),
        sa.Column('total_price', sa.Float, nullable=False),
        sa.Column('discount_code_id', sa.Integer, sa.ForeignKey('discount_code.id')),
        sa.Column('worker_id', sa.Integer, sa.ForeignKey('worker.id')),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('client.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'bill_product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('bill_id', sa.Integer, sa.ForeignKey('bill.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'delivery_bill',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address_id', sa.Integer, sa.ForeignKey('address.id')),
        sa.Column('bill_id', sa.Integer, sa.ForeignKey('bill.id')),
        sa.Column('status', sa.String(25), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'delivery_order',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address_id', sa.Integer, sa.ForeignKey('address.id')),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('order.id')),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    op.create_table(
        'menu',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, onupdate=datetime.now(), default=datetime.now()),
    )

    

    # CREATE TABLE Menu
    # (
    # ID        INT     NOT NULL,
    # name      VARCHAR NULL    ,
    # is_active BOOLEAN NULL    ,
    # PRIMARY KEY (ID)
    # );

    # CREATE TABLE Menu Section
    # (
    # ID                INT     NOT NULL,
    # name              VARCHAR NULL    ,
    # description       VARCHAR NULL    ,
    # menu_id           INT     NOT NULL,
    # position          INT     NULL    ,
    # regex_date_active VARCHAR NULL     COMMENT 'This could be regex or different fields',
    # PRIMARY KEY (ID)
    # );


    # CREATE TABLE Section Product
    # (
    # ID         INT NOT NULL,
    # position   INT NULL    ,
    # section_id INT NOT NULL,
    # product_id INT NOT NULL,
    # PRIMARY KEY (ID)
    # );



    


def downgrade():
    op.drop_table('user')
