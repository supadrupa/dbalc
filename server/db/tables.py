from sqlalchemy import MetaData, Table, Integer, Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

account_table = Table(
    'account', metadata,
    Column('id', UUID, primary_key=True),
    Column('avatar', String, nullable=False),
    Column('proxy', String, nullable=False),
    Column('client_id', Integer, nullable=False),
    Column('created_at', DateTime(True), nullable=False),
    Column('domain', String),
    Column('position', String),
    Column('is_archived', Boolean),

    schema="accounts"
)

