"""auto-vote

Revision ID: 1736ef74c1ae
Revises: cd03fcc65d22
Create Date: 2021-12-29 20:50:42.239991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1736ef74c1ae'
down_revision = 'cd03fcc65d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
