#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, count
from pyspark.sql.types import StringType

def ejercicio():
    # Inicia una sesión de Spark
    spark = SparkSession.builder.appName("PokemonAnalysis").getOrCreate()
    
    # Carga el archivo CSV en un DataFrame de PySpark
    pokemon = spark.read.csv("C:\\Users\\Bertani\\Downloads\\pokemon.csv", header=True, inferSchema=True)
    
    # Filtra y quita los que `Name` empieza con "Mega"
    pokemon = pokemon.filter(~col("Name").startswith("Mega"))
    
    # Quita también a los Legendary
    no_legendary = pokemon.filter(col("Legendary") == False)
    
    # Calcula la velocidad al doble
    doble = no_legendary.withColumn("Double_Speed", col("Speed") * 2)
    
    # Filtra y queda solo con aquellos cuya `Double_Speed` es mayor que 100
    mayor100 = doble.filter(col("Double_Speed") > 100)
    
    # Cuenta cuántos quedan por `Generation`
    Generation = mayor100.groupBy("Generation").agg(count("*").alias("Conteo"))
    
    # Ordena por `Generation`
    ordena = Generation.orderBy("Generation")
    
    # Cambia el tipo de dato de `Conteo` para que sea String
    Final = ordena.withColumn("Conteo", col("Conteo").cast(StringType()))
    
    # Muestra el resultado final
    Final.show()
    
    # Devuelve el DataFrame final
    return Final

pokemon=ejercicio()
print(pokemon)


# In[ ]:




