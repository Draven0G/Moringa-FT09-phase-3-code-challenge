class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.create_author_in_db()


    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("Id must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = value

    def create_author_in_db(self):
        # implement database insertion logic here
        pass

    def articles(self):
        # implement SQL JOINS logic to retrieve articles associated with the author
        pass

    def magazines(self):
        # implement SQL JOINS logic to retrieve magazines associated with the author
        pass