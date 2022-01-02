"""add content to post table

Revision ID: ef0b5d425f6b
Revises: b12691743eb8
Create Date: 2021-12-29 19:48:56.653154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef0b5d425f6b'
down_revision = 'b12691743eb8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
