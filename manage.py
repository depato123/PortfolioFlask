from flask_script import Manager
from portfolio.main import app, db

manager = Manager(app)
app.config['DEBUG'] = True

@manager.command
def create_tables():
    """ Creamos tablas de bases de datos """
    db.create_all()

if __name__ == '__main__':
    manager.run()


#########################
# 
#  <link rel="stylesheet" href="css/normalize.css">
#  <link rel="stylesheet" href="css/style.css">