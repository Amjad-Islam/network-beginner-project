# Network Basics Lab

A small, hands-on introduction to computer networking with Python. Build a TCP echo server and client, then use a simple TCP port checker to see which ports accept connections.

## Features

- TCP echo server listening on `127.0.0.1:5000`
- Command-line client for sending a message to the server
- Basic TCP port checker with configurable host and ports
- Uses only Python's standard library; no third-party packages required

## Requirements

- Python 3
- Two terminal windows for the server and client demonstration

Check that Python is available:

```powershell
python --version
```

On systems where the Python command is named `python3`, use `python3` in place of `python` in the instructions below.

## Getting started

Open a terminal in this project directory.

### 1. Start the server

In the first terminal, run:

```powershell
python server.py
```

The server should report:

```text
Server listening on 127.0.0.1:5000
```

Keep this terminal open while you use the client and port checker.

### 2. Send a message from the client

In a second terminal, run:

```powershell
python client.py --host 127.0.0.1 --port 5000 --message "Hello from a beginner network project!"
```

The client prints the server's reply:

```text
Echo: Hello from a beginner network project!
```

The server also prints the client's address and the message it received.

### 3. Check ports on your local machine

With the server still running, use the port checker in the second terminal:

```powershell
python network_lab.py --host 127.0.0.1 --ports 20,21,22,80,5000
```

Port `5000` should show as open while the server is running. Other ports may be open or closed depending on services running on your machine.

## Project structure

| File | Description |
| --- | --- |
| `server.py` | Accepts TCP connections on `127.0.0.1:5000` and echoes one received message. |
| `client.py` | Connects to a host and port, sends a message, and prints the response. |
| `network_lab.py` | Attempts TCP connections to a comma-separated list of ports and reports the result. |

## Command options

### Client

```text
python client.py --host HOST --port PORT --message MESSAGE
```

- `--host`: server IP address or hostname (default: `127.0.0.1`)
- `--port`: server port (default: `5000`)
- `--message`: text to send (default: `Hello from client!`)

### Port checker

```text
python network_lab.py --host HOST --ports PORT,PORT,...
```

- `--host`: host to check (default: `127.0.0.1`)
- `--ports`: comma-separated TCP ports (default: `20,21,22,80,443,5000`)

The checker tests TCP connections only. A result of `closed` means a connection could not be established; it does not identify why the connection failed.

## Networking concepts

- **IP address** identifies a device or network interface. `127.0.0.1` is the loopback address, meaning your own computer.
- **Port** identifies a service endpoint on a device. This server uses port `5000`.
- **Client and server**: the server waits for connections; the client initiates one.
- **TCP** provides a connection-oriented byte stream. This project uses TCP for both messaging and port checks.

## Safety and scope

The server binds to `127.0.0.1`, so it accepts connections from the same computer only. The port checker makes connection attempts to the host and ports you specify. Use it only on your own devices or on systems you have explicit permission to test.

## Ideas for extending the lab

- Add input validation for port numbers.
- Let the server handle multiple messages on one connection.
- Add a UDP client/server example and compare it with TCP.
- Add a DNS lookup exercise using Python's `socket` module.
- Improve the port checker to accept port ranges and report connection errors more precisely.
