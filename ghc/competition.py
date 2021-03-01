# Escribir en este archivo todo el codigo especifico para resolver el problema
# de la competencia.

PROBLEM_NAME = '<problem>'   # llenar con el nombre del problema
YEAR = '<year>'              # llenar con el año de la competencia




# Escribe los datos contenidos en data en un archivo de texto en la direccion
# especificada por filename.
# filename (str):   ruta completa del archivo que sera creado
# data (any):       los datos a almacenar en el archivo
def write_output_file(filename, 
                      data):
  file = open(filename, 'wt')
  # escribir los datos de salida en el archivo
  # llenar con la logica especifica del problema de la competencia
  file.close()
