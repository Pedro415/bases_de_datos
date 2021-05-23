import psycopg2
class Connection: 
    def __init__(self):
        self.connection = None 
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5433",dbname="pry4",user="postgres",password="1234")
        except Exception as e:
            print (e)
    def closeConnection(self):
        self.connection.close()
        
        