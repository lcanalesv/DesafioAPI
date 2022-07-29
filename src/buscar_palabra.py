
#Función para crear buscar una palabra en un archivo de Google Drive
def buscar_en_archivo(id_documento,userEmail,creds):
    file = creds.CreateFile({'id': id_documento})
    content = file.GetContentString()
    if(userEmail in content):
        return "encontrado"
    else:
        return "no encontrado"