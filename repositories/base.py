from databases import databases

class BaseRepository:
    def __init__(self, database: Database):
        self.database = database
        