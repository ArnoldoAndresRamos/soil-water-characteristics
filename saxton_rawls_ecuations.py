
import math

def calcular_humedad_a_1500kPa( arena , arcilla , materia_organica):
  """
  Descripcion:
    calcula la humedad del suelo a una tensión de -1500 Kpa fraccion 

  Parametros:
    arena   = contenido de arena del suelo fraccion 
    arcilla = contenido de arcilla del suelo fraccion 
    materi_organica = contenido de materia organica del suelo porcentaje wt

  retorna:
    humedad_a_1500KPa " en fraccion de Volumen m3 agua/ m3 suelo "
  """
  a , b , c , d , e , f , g = -0.024 , 0.487 ,0.006 , 0.005,  0.013 , 0.068 , 0.031
  u1500t = a * arena + b * arcilla + c * materia_organica + d*(arena * materia_organica) - e * (arcilla * materia_organica) + f *(arena * arcilla) + g
  humedad_suelo_a_1500KPa = u1500t + (0.14 * u1500t - 0.02)

  return humedad_suelo_a_1500KPa



def calcular_humedad_a_33kPa( arena , arcilla , materia_organica ):
  """
  Descripcion:
    calcuala la humedad del suelo a la tensión de -33 KPa
  
  Parametros:
    arena   = contenido de arena del suelo fraccion 
    arcilla = contenido de arcilla del suelo fraccion 
    materi_organica = contenido de materia organica del suelo porcentaje wt
  
  retorna:
    humedad_suelo_a_33KPa "en fraccion, m3 agua/ m3 suelo "

  """
  a, b, c, d, e, f, g =  -0.251 , 0.195 , 0.011, 0.006 , 0.027 , 0.452 , 0.299
  u33t = a * arena + b * arcilla + c * materia_organica + d * (arena * materia_organica) - e*(arcilla * materia_organica) + f*(arena * arcilla) + g
  humedad_suelo_a_33KPa  = u33t + (1.283*(u33t)**2 - 0.374*(u33t) - 0.015)

  return humedad_suelo_a_33KPa 


calcular_humedad_a_33kPa( 0.84, 0.1 , 2.5)