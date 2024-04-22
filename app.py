from http.server import HTTPServer, SimpleHTTPRequestHandler
def run(server_class = HTTPServer, handler_class = SimpleHTTPRequestHandler):
    try:
        server_address = ('',8000)
        httpd = server_class(server_address, handler_class)
        print ('Iniciando Servidor web en http://localhost:8000/')
        httpd.serve_forever(0)
    except KeyboardInterrupt:
        print('Apagando Servidor web')
        httpd.socke.close()
if __name__ == "__main__":
    run() 