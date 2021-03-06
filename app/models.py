from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    # back是反向引用,User和Post是一对多的关系，backref是表示在Post中新建一个属性author，关联的是Post中的user_id外键关联的User对象。
    #lazy属性常用的值的含义，select就是访问到属性的时候，就会全部加载该属性的数据;joined则是在对关联的两个表进行join操作，从而获取到所有相关的对象;dynamic则不一样，在访问属性的时候，并没有在内存中加载数据，而是返回一个query对象, 需要执行相应方法才可以获取对象，比如.all()
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<用户名:{}>'.format(self.username)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db .Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Item(db.Model):
    __tablename__ = 'item'
    item_id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.String(64),index=True,unique=True)
    item_type = db.Column(db.Integer,primary_key=True)
    price = db.Column(db.Integer,primary_key=True)
    total_price = db.Column(db.Integer,primary_key=True)
    des1 = db.Column(db.String(120),index=True,unique=True)
    des2 = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return '<物品:{}>'.format(self.item_name)
