from flask_mongoengine import MongoEngine

db = MongoEngine()

class Role(db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document):
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def is_authenticated(self):
        return True if self.active else False

    def is_active(self):
        return self.active
    
    def get_id(self):
        return str(self.id)
