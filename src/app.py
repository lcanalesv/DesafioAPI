from flask import Flask, request, redirect, Response, json
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from buscar_palabra import buscar_en_archivo
from crear_archivo import crear_archivo_texto

app = Flask(__name__)
gauth = GoogleAuth()

#Realiza la autenticación oauth2
@app.route('/')
def getAuth():
    if gauth.credentials is None:
        auth_url = gauth.GetAuthUrl()
        return redirect(auth_url)
    else:
        return 'Registrado Exitosamente'

#Ruta callback post autenticación oauth
@app.route('/oauth2callback')
def callback():
    code = request.args.get('code')
    gauth.Auth(code)
    return redirect('/')   

#Modulo para buscar documento y contenido del mismo
@app.route('/search-in-doc', methods=['GET'])
def search_userEmail():
    id_documento = request.args.get('id_documento', None)
    userEmail = request.args.get('userEmail', None)
    creds = GoogleDrive(gauth)
    respuesta = buscar_en_archivo(id_documento,userEmail,creds)
    if respuesta == "encontrado":
        return Response(status=200)
    else:
        return Response(status=500)

#Modulo para carga de archivos, tomando como parámetro el título y descripción del archivo.
@app.route('/file', methods=['POST'])
def upload_file():
    data = request.get_json()
    try:
        titulo = data['titulo']
        descripcion = data['descripcion']
        creds = GoogleDrive(gauth)
        respuesta = crear_archivo_texto(titulo,descripcion,creds)
    except:
        respuesta = {'estado':'error en parametro'}
        json.dumps(respuesta)

    respuesta = json.loads(respuesta)
    if respuesta['estado'] == 'cargado':
        data = '{"id":"',respuesta['id'],'", "titulo":"',respuesta['titulo'],'", "descripcion":"',respuesta['descripcion'],'"}'
        return Response(data, status=200, mimetype='application/json')
    elif respuesta['estado'] == 'error en parametro':
        return Response('{"result":"Error!"}',status=404, mimetype='application/json')
    elif respuesta['estado'] == 'no cargado':
        return Response('{"result":"No Cargado!"}',status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)