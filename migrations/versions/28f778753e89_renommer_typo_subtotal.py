"""renommer typo subtotal

Revision ID: 28f778753e89
Revises: 8bc06ca1b5f6
Create Date: 2021-07-23 02:04:24.589343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f778753e89'
down_revision = '8bc06ca1b5f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('facture', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subtotal', sa.Float(), nullable=True))
        batch_op.drop_column('sub_total')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('facture', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sub_total', sa.FLOAT(), nullable=True))
        batch_op.drop_column('subtotal')

    # ### end Alembic commands ###
