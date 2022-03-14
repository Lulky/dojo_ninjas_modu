from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    
    @classmethod
    def muestra_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_dojo_ninja').query_db(query)
        dojos = []
        for c in results:
            dojos.append( cls(c) )
        return dojos
    
    @classmethod
    def guardar_dojos(cls, data):
        
        query = "INSERT INTO dojos (name) VALUES (%(name)s);" 
        result = connectToMySQL('esquema_dojo_ninja').query_db(query, data)
        
        return result

    @classmethod
    def obtener_un_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('esquema_dojo_ninja').query_db(query, data)
        dojo = cls(results[0])
        for fila in results:
            n = {
                'id': fila['id'],
                'first_name': fila['first_name'],
                'last_name': fila['last_name'],
                'age': fila['age'],
                'created_at': fila['created_at'],
                'updated_at': fila['updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo    


        