import obj.init
import obj.connections

class dataSQL:
    def __init__(self, connection, query):
        mode = query.split()[0].lower()
        if mode=='select':
            self.data = connection.cursor().execute(query).fetchall()
        else:
            self.commit = connection.cursor().execute(query)
            connection.commit()
