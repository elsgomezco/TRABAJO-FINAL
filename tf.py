import pandas as pd

archivo = "datos_limpios.csv"
df = pd.read_csv(archivo)

bienvenido = input("Bienvenido al programa de caracterización de la calidad del agua de estaciones de monitoreo del río Cauca")

def menu_opciones(df):
    while True:
        eleccion = input("Defina una de las siguientes opciones que desea realizar:\n"
                        "1. Calcular la calidad del agua de n estaciones con ICA\n"
                        "2. Calcular la estadística descriptiva de n estaciones\n")   

        # Obtener valores únicos de la primera columna y convertirlos en un conjunto
        valores_unicos = set(df.iloc[:, 1])

        # Ordenar los valores únicos y asignar un ID a cada valor
        valores_ordenados = sorted(valores_unicos, reverse=True)
        valores_con_id = {idx + 1: valor for idx, valor in enumerate(valores_ordenados)}

        # O también puedes usar el método join para imprimir la lista en una sola cadena con saltos de línea
        lista_con_saltos = "\n".join([f"{idx}: {valor}" for idx, valor in valores_con_id.items()])

        if eleccion == "1":
            while True:
                try:
                    x = input("Seleccione las estaciones para calcular la calidad del agua \n"
                            f"{lista_con_saltos}")
                    
                    if 1 <= int(x) <= 19:
                        print("Cargando el calculo ICA...")

                        
                    else:
                        print("digite los numeros de 1 a 19, según la estación deseada")
                        continue
                    break
                except:
                    print("Solo digite valores numericos del 1 al 19, según la estación deseada")
        
        
                #else:
                    #print("digite los numeros de 1 a 19, según la estación deseada")
            break
        elif eleccion == "2":
            while True:
                try:
                    y = input("Seleccione las estaciones para calcular la estadística descriptiva:\n"
                            f"{lista_con_saltos}\n")
                    if 1 <= int(y) <= 19:
                        print("continuando con el programa")
                        #continue
    # ESTADISTICA DESCRIPTIVA
                        # Crear un DataFrame temporal para almacenar los datos de las estaciones seleccionadas
                        datos_estaciones_seleccionadas = pd.DataFrame()
                        # Convertir la elección del usuario a una lista de números de estaciones
                        numeros_estaciones = [int(valor.strip().split(":")[0]) for valor in y.split("\n") if valor.strip().split(":")[0].isdigit()]
                        # Iterar sobre los números de estaciones seleccionadas
                        for num_estacion in numeros_estaciones:
                            # Obtener el nombre de la estación asociada al número
                            nombre_estacion = valores_con_id.get(num_estacion)  # valores_con_id es el diccionario que contiene los nombres de las estaciones asociados a sus números
                            
                            # Filtrar el DataFrame original para obtener solo los datos de la estación actual
                            datos_estacion_actual = df[df['ESTACIONES'] == nombre_estacion]  # Reemplaza 'Nombre_de_la_Columna' con el nombre real de la columna de estaciones
                            
                            # Agregar los datos de la estación actual al DataFrame temporal
                            datos_estaciones_seleccionadas = pd.concat([datos_estaciones_seleccionadas, datos_estacion_actual], ignore_index=True)
                        
                            # Calcular estadísticas descriptivas para todas las columnas numéricas de las estaciones seleccionadas
                            descripcion = datos_estaciones_seleccionadas.describe()
                        
                            # Mostrar las estadísticas descriptivas
                            print(f"\nEstadísticas descriptivas para las estación {nombre_estacion}:\n{descripcion}")
                
                    else:
                        print("digite los numeros de 1 a 19, según la estación deseada")
                        continue
                    break    
                except: 
                    print("Solo digite valores numericos del 1 al 19, según la estación deseada")                
            break
            
        else:
            print("Debe seleccionar 1 o 2. Intente nuevamente.")

# Uso de la función:
eleccion_usuario = menu_opciones(df)
