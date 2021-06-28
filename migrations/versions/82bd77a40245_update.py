"""update

Revision ID: 82bd77a40245
Revises: d1d6cbaf4784
Create Date: 2021-06-28 16:24:26.511764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82bd77a40245'
down_revision = 'd1d6cbaf4784'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('facture', sa.Column('name', sa.String(length=50), nullable=True))
    op.add_column('facture', sa.Column('amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('facture', 'amount')
    op.drop_column('facture', 'name')
    # ### end Alembic commands ###