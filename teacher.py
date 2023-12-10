from manager import Manager

class Teacher(Manager):

    def __init__(self, db, collection):
        super().__init__(db, collection)