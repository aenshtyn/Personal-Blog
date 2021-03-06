"""update of user class

Revision ID: 230fa61616f7
Revises: 9fa7403c980d
Create Date: 2020-05-10 11:56:30.850521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230fa61616f7'
down_revision = '9fa7403c980d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
