from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__: "user"

    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(120), unique=False, nullable=False)
    _is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return f'User is {self.USER}, id: {self.id}'


    def to_dict(self):
        return{
            'id': self.id,
            'nick': self.nick,
            'tasks': [task.to_dict() for task in tasks]
            }

    def create(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_by_id(clas, id_user):
        task = clas.query.filter_by(id = id_user).one_or_none()
        return task


    @classmethod
    def get_all(cls):
        users = cls.query.all()
        return users
        
    
    def delete_user(self):
        self._is_active=False
        db.session.commit()
        return self
        

    


class Task(db.Model):
    __tablename__: "task"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def __repr__(self):
        return f'Task is {self.task}, {self.done}, from {self.user_id}, id: {self.id}'

   
    def to_dict(self):
        return{
            'task': self.task,
            'done': self.done,
        }


    def create(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def get_by_id(clas, id):
        task = clas.query.get(id)
        return task

   
    @classmethod
    def get_by_user(cls, user_id):
        tasks = cls.query.filter_by(user_id)
        return tasks
    

    @classmethod
    def get_all(cls):
        users = cls.query.all()
        return users


    def delete_task(self):
        db.session.delete(self)
        db.session.commit()
        return self