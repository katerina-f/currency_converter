from http.server import ThreadingHTTPServer
import logger
from converter import ConverterHTTPServer

HOST_NAME = "0.0.0.0"
SERVER_PORT = 8080


if __name__ == "__main__":
    logger = logger.get_custom_logger(__name__)

    web_server = ThreadingHTTPServer((HOST_NAME, SERVER_PORT), ConverterHTTPServer)
    logger.info(f"Server started http://{HOST_NAME}:{SERVER_PORT}")

    try:
        web_server.serve_forever()
    finally:
        web_server.server_close()
