"""empty message

Revision ID: 81fab52fcd8b
Revises: 
Create Date: 2017-02-05 15:51:19.926839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81fab52fcd8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('url', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('brand', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    # ### end Alembic commands ###
