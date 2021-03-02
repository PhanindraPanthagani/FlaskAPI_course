from app import db


class Task(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    date = db.Column(db.Date,nullable = False)

    def __rep__(self):
        #This function is going to represent each instance
        #of this data model
        return f'{self.title} created on {self.date}'

        
