from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=45)),
    Column('phone', Integer),
    Column('passwd', String(length=200)),
    Column('email', String(length=50)),
    Column('idNumber', String(length=40)),
    Column('gender', SmallInteger),
    Column('birthday', Date),
    Column('level', Integer),
)

trust_product_preorder = Table('trust_product_preorder', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=45)),
    Column('phone', Integer),
    Column('product_id', Integer),
    Column('user_id', Integer),
    Column('status', SmallInteger),
    Column('createTime', DateTime),
    Column('updateTime', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].create()
    post_meta.tables['trust_product_preorder'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].drop()
    post_meta.tables['trust_product_preorder'].columns['user_id'].drop()
