from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(4000))
    def __repr__(self):
        return "<Title: {} body: {}>".format(self.title,self.body)