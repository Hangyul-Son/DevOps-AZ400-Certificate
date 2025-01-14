"""Add visa related tables to the db

Revision ID: ef37e0672c8d
Revises: 2c99ef9f2ca5
Create Date: 2024-07-15 22:13:27.327734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef37e0672c8d'
down_revision = '2c99ef9f2ca5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('purpose',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('visa_cost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visa_id', sa.Integer(), nullable=False),
    sa.Column('entry_frequency', sa.String(length=64), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.ForeignKeyConstraint(['visa_id'], ['visa_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visa_document',
    sa.Column('visa_id', sa.Integer(), nullable=False),
    sa.Column('document_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['document_id'], ['document.id'], ),
    sa.ForeignKeyConstraint(['visa_id'], ['visa_info.id'], ),
    sa.PrimaryKeyConstraint('visa_id', 'document_id')
    )
    op.create_table('visa_purpose',
    sa.Column('visa_id', sa.Integer(), nullable=False),
    sa.Column('purpose_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['purpose_id'], ['purpose.id'], ),
    sa.ForeignKeyConstraint(['visa_id'], ['visa_info.id'], ),
    sa.PrimaryKeyConstraint('visa_id', 'purpose_id')
    )
    with op.batch_alter_table('visa_info', schema=None) as batch_op:
        batch_op.drop_column('cost')
        batch_op.drop_column('visa_purpose')
        batch_op.drop_column('currency')
        batch_op.drop_column('entry_frequency')
        batch_op.drop_column('required_documents')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visa_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('required_documents', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('entry_frequency', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('currency', sa.VARCHAR(length=3), nullable=True))
        batch_op.add_column(sa.Column('visa_purpose', sa.VARCHAR(length=64), nullable=True))
        batch_op.add_column(sa.Column('cost', sa.FLOAT(), nullable=True))

    op.drop_table('visa_purpose')
    op.drop_table('visa_document')
    op.drop_table('visa_cost')
    op.drop_table('purpose')
    op.drop_table('document')
    # ### end Alembic commands ###
