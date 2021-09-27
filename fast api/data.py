import sqlalchemy as db
def connection(data):
    db_pass="Py,90$56gf"
    engine = db.create_engine('mysql+mysqldb://python:'+db_pass+'@localhost/contacts')
    connection = engine.connect()
    metadata = db.MetaData()
    if(data == 'connection'):
        return connection
    if(data == 'metadata'):
        return metadata
    if(data == 'engine'):
        return engine
def Contactinfo():
    Contacts = db.Table('Contacts', connection('metadata'), autoload=True, autoload_with=connection('engine'))
    query = db.select([Contacts])
    ResultProxy = connection('connection').execute(query)
    ResultSet = ResultProxy.fetchall()
    return ResultSet
def insert_employee():
    emp = db.Table('emp', connection('metadata'),
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )
    #metadata.create_all(engine) #Creates the table
    #Inserting record one by one
    query = db.insert(emp).values(Id=2, name='naveen', salary=60000.00, active=True)
    ResultProxy = connection('connection').execute(query)
