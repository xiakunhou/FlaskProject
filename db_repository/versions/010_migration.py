from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trust_product = Table('trust_product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('reason', String(length=50)),
    Column('threshold', Integer),
    Column('dueTime', Integer),
    Column('shortDesc', String(length=200)),
    Column('profitRate', Float),
    Column('profitType', String(length=50)),
    Column('profitClose', String(length=50)),
    Column('profitDesc', String(length=300)),
    Column('status', SmallInteger),
    Column('organization', String(length=50)),
    Column('investType', String(length=50)),
    Column('investArea', String(length=50)),
    Column('total', Integer),
    Column('detailDesc', String(length=500)),
    Column('riskControl', String(length=500)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trust_product'].columns['profitClose'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trust_product'].columns['profitClose'].drop()
