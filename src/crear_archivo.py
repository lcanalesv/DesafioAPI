import json

#Función para crear archivo en Google Drive
def crear_archivo_texto(titulo,descripcion,creds):
#En caso de que el archivo se cargue exitosamente, se devuelve el estado de "cargado", id de documento, titulo y descripción en formato json
    try:
        archivo = creds.CreateFile({'title': titulo})
        archivo.SetContentString(descripcion)
        archivo.Upload()
        estado = 'cargado'
        id = archivo['id']
        data = {
            'estado': estado,
            'id': id,
            'titulo': titulo,
            'descripcion': descripcion,
        }
        return json.dumps(data)
#En caso de que exista algún error en la carga, se devuelve el estado de "no cargado"
    except:
        estado = 'no cargado'
        data = {
            'estado': estado,
        }