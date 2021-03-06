"""create account

Revision ID: ed0a8b560027
Revises: 
Create Date: 2019-10-15 18:11:07.054525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ed0a8b560027'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("create schema accounts")

    op.create_table('account',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('avatar', sa.String(), nullable=False),
    sa.Column('proxy', sa.String(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('domain', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('is_archived', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='accounts'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account', schema='accounts')
    # ### end Alembic commands ###
