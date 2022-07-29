1. Ejecutar los siguientes comandos en Docker 

    docker build -t desafio_google:v1 .
    docker run -it --publish 5001:5001 desafio_google:v1

2. En la aplicación ir al navegador e ingresar a http://localhost:5001 y realizar la autenticación oauth.

3. Una vez completada la autenticación, puede hacer uso de la API.

Buscar palabra en documento:

    - En el navegador: http://localhost:5001/search-in-doc?id_documento=<id_documento>1&userEmail=<palabra>
    - Reemplazar <id_documento> por el id de documento a buscar
    - Reemplazar <palabra> por la palabra a buscar en el documento

Subir documento:

    - A través de curl ingresar lo siguiente:
        curl -iX POST http://localhost:5001/file -d '{"titulo":"<titulo_doc>", "descripcion":"<descripcion_doc>"}' -H 'Content-Type: application/json'
    - Reemplazar <titulo_doc> por el titulo del documento a cargar.
    - Reemplazar <descripcion_doc> por la descripcion del documento a cargar.