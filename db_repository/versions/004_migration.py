from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('threshold', Integer),
    Column('dueTime', String(length=20)),
    Column('shortDesc', String(length=128)),
    Column('profitRate', Float),
    Column('profitType', String(length=45)),
    Column('profitDesc', String(length=255)),
    Column('status', SmallInteger),
    Column('organization', String(length=45)),
    Column('investType', String(length=45)),
    Column('investArea', String(length=45)),
    Column('total', Integer),
    Column('detailDesc', String(length=256)),
    Column('riskControl', String(length=256)),
    Column('nav', Float),
    Column('startDate', Date),
    Column('broker', String(length=45)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].columns['broker'].create()
    post_meta.tables['product'].columns['nav'].create()
    post_meta.tables['product'].columns['startDate'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].columns['broker'].drop()
    post_meta.tables['product'].columns['nav'].drop()
    post_meta.tables['product'].columns['startDate'].drop()
