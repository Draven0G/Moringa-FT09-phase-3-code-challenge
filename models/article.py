class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.create_article_in_db()


    def __repr__(self):
        return f'<Article {self.title}>'
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed after instantiation")
        self._title = value

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def create_article_in_db(self):
        # implement database insertion logic here
        pass
