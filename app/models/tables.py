from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(4000))
    def __repr__(self):
        return "<Title: {} body: {}>".format(self.title,self.body)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    number_of_pages = db.Column(db.Integer)
    rate = db.Column(db.Float)
    def __repr__(self):
        return "<Title: {} Number of pages: {} rate {}>".format(self.title,self.number_of_pages,self.rate)
