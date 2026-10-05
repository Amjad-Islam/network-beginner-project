import argparse
import socket


def is_port_open(host, port, timeout=1):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def scan_ports(host, ports):
    results = []
    for port in ports:
        if is_port_open(host, port):
            results.append((port, "open"))
        else:
            results.append((port, "closed"))
    return results


def main():
    parser = argparse.ArgumentParser(description="Basic network scan for beginners")
    parser.add_argument("--host", default="127.0.0.1", help="Target host to scan")
    parser.add_argument("--ports", default="20,21,22,80,443,5000", help="Comma-separated list of ports")
    args = parser.parse_args()

    ports = [int(port.strip()) for port in args.ports.split(",") if port.strip()]
    print(f"Scanning {args.host} for ports: {ports}")

    for port, status in scan_ports(args.host, ports):
        print(f"Port {port}: {status}")


if __name__ == "__main__":
    main()
