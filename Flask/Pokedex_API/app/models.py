from app import db 

class Pokemon(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    cuteness_rating = db.Column(db.Integer, nullable=False)
    
    def __repr__(self): 
        return f"<Pokemon {self.name}>"