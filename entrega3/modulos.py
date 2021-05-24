
def consulta1():
    return "select llamada.anio, loc.nombre, sum(llamada.acumulado_incidentes) as llamadas_recibidas " \
           "from llamada join upz on (llamada.id_upz = upz.id) join localidad loc on (upz.id_localidad = loc.id) " \
           "where anio = 2020 group by llamada.anio, loc.nombre " \
           "order by llamada.anio asc, llamadas_recibidas desc"

def consulta2():
    return "(select llam.anio as anio, inc.tipo as incidente, sum(llam.acumulado_incidentes) as total " \
            "from incidente inc join llamada llam on (inc.codigo = llam.codigo_incidente) " \
            "where llam.anio = 2020 and inc.tipo != '-' group by anio, incidente order by total desc)"

def consulta3():
    return "select llam.mes as mes, sum(llam.acumulado_incidentes) as total " \
           "from llamada llam " \
           "where llam.anio = 2020 group by mes"

def consulta4():
    return "select upz.nombre, sum(llam.acumulado_incidentes) as total " \
            "from upz join llamada llam on (upz.id = llam.id_upz) " \
            "join incidente inc on (llam.codigo_incidente = inc.codigo) " \
            "where upz.nombre!='SIN LOCALIZACION' and " \
            "inc.tipo = 'ATRACO / HURTO EN PROCESO' or inc.tipo = 'HURTO EFECTUADO' " \
            "group by upz.nombre order by total desc"

import psycopg2

class Connection:

    def __init__(self):
        self.connection = None

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="proyecto_bd",user="postgres",
                                               password="postgres")
        except Exception as e:
            print(e)

    def closeConnection(self):
        self.connection.close()
"""
con = psycopg2.connect(host="localhost",port="5432",dbname="proyecto_bd",user="postgres",password="postgres")
print("Database opened successfully")

cur = con.cursor()

cur.execute(consulta1)
rows = cur.fetchall()

for row in rows:
    print("ANIO =", row[0])
    print("MES =", row[1])
    print("NOMBRE =", row[2])
    print("TOTAL LLAMADAS =", row[3], "\n")


print("Operation done successfully")
con.close()
"""
