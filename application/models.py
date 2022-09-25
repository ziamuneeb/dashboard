from application import db




class Expense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(100), nullable = False)
    type = db.Column(db.String(100), nullable= False)
    category = db.Column(db.String(100), nullable= False)
    amount = db.Column(db.String(50), nullable= False)
    
    def __repr__(self):
        return '<User %r>' % self.id
    

db.create_all()



