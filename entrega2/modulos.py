
import psycopg2

con = psycopg2.connect(host="localhost",port="5432",dbname="proyecto_bd",user="postgres",password="postgres")
print("Database opened successfully")

cur = con.cursor()

query = " select llamada.anio, llamada.mes, loc.nombre, sum(llamada.acumulado_incidentes) as llamadas_recibidas from llamada join upz on (llamada.id_upz = upz.id) join localidad loc on (upz.id_localidad = loc.id) where anio = 2020 group by llamada.anio, llamada.mes, loc.nombre order by mes asc, llamadas_recibidas desc "
cur.execute(query)
rows = cur.fetchall()

for row in rows:
    print("ANIO =", row[0])
    print("MES =", row[1])
    print("NOMBRE =", row[2])
    print("TOTAL LLAMADAS =", row[3], "\n")


print("Operation done successfully")
con.close()
