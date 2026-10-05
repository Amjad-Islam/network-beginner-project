# Network Basics Lab

This project is designed for a complete beginner who wants to learn the basics of networking using Python's standard library.

## What you will build

- A simple TCP server that listens for connections
- A client that connects to the server and sends a message
- A small port scanner that checks whether common ports are open

## Project files

- `server.py` - a simple echo server
- `client.py` - connects to a server and sends data
- `network_lab.py` - scans ports and checks basic connectivity

## Quick start

1. Open a terminal in this project folder.
2. Start the server:

   python server.py

3. In another terminal, connect with the client:

   python client.py --host 127.0.0.1 --port 5000 --message "Hello from a beginner network project!"

4. Run a basic port scan:

   python network_lab.py --host 127.0.0.1 --ports 20,21,22,80,5000

## What to learn

- `socket` lets programs communicate over a network
- A server listens on a port
- A client connects to that port
- Ports are like doors for different services
- `TCP` is connection-based and reliable
- `UDP` is lighter and often faster, but less reliable

## Example output

When the client sends a message, the server echoes it back.

```
Server listening on 127.0.0.1:5000
Client connected from ('127.0.0.1', 12345)
Received: Hello from a beginner network project!
```

## Next steps

- Try changing the port number
- Add a `UDP` example
- Scan a real public website like `example.com`
- Learn how IP addresses and DNS work

## Notes

This project uses only Python's built-in modules, so it is beginner-friendly and does not require any installation.
