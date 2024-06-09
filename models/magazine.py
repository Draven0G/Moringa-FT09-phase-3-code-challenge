class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.create_magazine_in_db()


    def __repr__(self):
        return f'<Magazine {self.name}>'
    
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
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def create_magazine_in_db(self):
        # implement database insertion logic here
        pass

    def articles(self):
        # implement SQL JOINS logic to retrieve articles associated with the magazine
        pass

    def contributors(self):
        # implement SQL JOINS logic to retrieve authors associated with the magazine
        pass

    def article_titles(self):
        # implement SQL JOINS logic to retrieve article titles associated with the magazine
        pass

    def contributing_authors(self):
        # implement SQL JOINS logic to retrieve authors who have written more than 2 articles for the magazine
        pass
