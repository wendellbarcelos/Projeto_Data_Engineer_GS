import psycopg2 as db
import csv


# Class para configurar ao DB
class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "dbgs",
                "password": "postgres",
                "host": "127.0.0.1",
                "database": "pydb"
            }
        }


# Metodo de conexão e cursor
class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Erro na conexão', e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class Pydb(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO respondente (nome, contrib_open_source, programa_hobby, salario) VALUES (%s,%s,%s,%s)"
            # sql = "INSERT INTO empresa (tamanho) VALUES (%s)"
            # sql = "INSERT INTO pais (nome) VALUES (%s)"
            # sql = "INSERT INTO ferramenta_comunic (nome) VALUES (%s)"
            # sql = "INSERT INTO linguagem_programacao (nome) VALUES (%s)"
            # sql = "INSERT INTO sistema_operacional (nome) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Erro ao inserir', e)

    
    def insert_csv(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding='utf-8'))
            for row in data:
                self.insert(row['Respondent'], row['OpenSource'], row['Hobby'], row['ConvertedSalary'])
                # self.insert(row['CompanySize'])
                # self.insert(row['Country'])
                # self.insert(row['CommunicationTools'])
                # self.insert(row['LanguageWorkedWith'])
                # self.insert(row['OperatingSystem'])
            print('Registro inserido')
        except Exception as e:
            print('Erro ao inserir csv', e)



if __name__ == "__main__":
    pydb = Pydb()
    pydb.insert_csv('carga_db.csv')