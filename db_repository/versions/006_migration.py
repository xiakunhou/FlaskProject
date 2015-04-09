from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
preorder = Table('preorder', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=45)),
    Column('phone', Integer),
    Column('product_id', Integer),
    Column('status', SmallInteger),
    Column('createTime', DateTime, default=ColumnDefault(datetime.datetime(2015, 4, 9, 16, 8, 26, 491305))),
    Column('updateTime', DateTime, default=ColumnDefault(datetime.datetime(2015, 4, 9, 16, 8, 26, 491357))),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['preorder'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['preorder'].drop()
