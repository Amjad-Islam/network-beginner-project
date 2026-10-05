import argparse
import socket


def send_message(host, port, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)
    client.connect((host, port))
    client.sendall(message.encode("utf-8"))
    response = client.recv(1024)
    print(response.decode("utf-8"))
    client.close()


def main():
    parser = argparse.ArgumentParser(description="Simple TCP client for a beginner network project")
    parser.add_argument("--host", default="127.0.0.1", help="Server IP address or hostname")
    parser.add_argument("--port", type=int, default=5000, help="Server port")
    parser.add_argument("--message", default="Hello from client!", help="Message to send to the server")
    args = parser.parse_args()
    send_message(args.host, args.port, args.message)


if __name__ == "__main__":
    main()
