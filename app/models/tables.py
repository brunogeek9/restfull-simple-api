from app import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    number_of_pages = db.Column(db.Integer)
    rate = db.Column(db.Float)
    def __repr__(self):
        return "<Title: {} Number of pages: {} rate {}>".format(self.title,self.number_of_pages,self.rate)
        