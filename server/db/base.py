from databases import Database


class Base:
    def __init__(self, database: Database):
        self._database = database
