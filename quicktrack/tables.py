from django_tables2 import Table, Column


class TrackingTable(Table):
    type = Column()
    date = Column()
    user = Column()
    description = Column()
    tags = Column()

    def render_tags(self, record):
        return ', '.join((str(t) for t in record.tags.all()))
