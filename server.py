from threading import Thread
from waitress import serve
from strender_backend.wsgi import application

def start_server():
    serve(application, port='8000')

if __name__ == '__main__':
    server_thread = Thread(target=start_server)
    server_thread.start()
    print("Server is running at http://localhost:8000")
