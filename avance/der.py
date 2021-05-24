def localidad():
 return """select id, nombre, total_habitantes
from localidad
order by nombre
"""
def enero():
 return """
select loc.nombre, sum(llamada.acumulado_incidentes) as llamadas_recibidas, llamada.mes
from llamada join upz on (llamada.id_upz = upz.id) join localidad loc on (upz.id_localidad = loc.id)
where anio = 2020 and mes =3 
group by loc.nombre, llamada.mes
order by loc.nombre
"""

def incidentesa():
 return """
select * 
from ((select inc.tipo as incidente, sum(llam.acumulado_incidentes) as total_2020, llam.anio
from incidente inc join llamada llam on (inc.codigo = llam.codigo_incidente)
where llam.anio = 2020 and tipo != '-' 
group by anio, incidente 
order by total_2020 desc
limit 20)
union all 
(select 'OTROS' as incidente, sum(total_2020) , 2020 as anio
from
(select inc.tipo as incidente, sum(llam.acumulado_incidentes) as total_2020, llam.anio
from incidente inc join llamada llam on (inc.codigo = llam.codigo_incidente)
where llam.anio = 2020 and tipo != '-' 
group by anio, incidente 
order by total_2020 desc
offset 20) as re))as derf
group by total_2020, incidente, anio
order by total_2020 desc

"""

def incidentesb():
 return """
select * 
from ((select inc.tipo as incidente, sum(llam.acumulado_incidentes) as total_2019, llam.anio
from incidente inc join llamada llam on (inc.codigo = llam.codigo_incidente)
where llam.anio = 2019 and tipo != '-' 
group by anio, incidente 
order by total_2019 desc
limit 20)
union all 
(select 'OTROS' as incidente, sum(total_2019) , 2019 as anio
from
(select inc.tipo as incidente, sum(llam.acumulado_incidentes) as total_2019, llam.anio
from incidente inc join llamada llam on (inc.codigo = llam.codigo_incidente)
where llam.anio = 2019 and tipo != '-' 
group by anio, incidente 
order by total_2019 desc
offset 20) as re))as derf
group by total_2019, incidente, anio
order by total_2019 desc

"""