import socket
import sys
import time


ALLOWED_HOSTS = {"127.0.0.1", "localhost", "scanme.nmap.org"}


def scan_port(host, port, timeout=1.0):
    """Return True if a port is open, False if it is closed."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(timeout)
            result = scanner.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        raise ValueError("Hostname could not be resolved.")
    except Exception as error:
        raise RuntimeError(f"Unexpected scanning error: {error}")


def validate_ports(start_port, end_port):
    """Validate the port range."""
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        raise ValueError("Port numbers must be between 1 and 65535.")
    if start_port > end_port:
        raise ValueError("Start port cannot be greater than end port.")


def validate_host(host):
    """Allow only approved hosts for this assignment."""
    if host not in ALLOWED_HOSTS:
        raise ValueError(
            "Unauthorized host. Only localhost, 127.0.0.1, and scanme.nmap.org are allowed."
        )


def port_scanner(host, start_port, end_port):
    """Scan a range of ports on an approved host."""
    validate_host(host)
    validate_ports(start_port, end_port)

    print(f"\n[SCANNER] Scanning host: {host}")
    print(f"[SCANNER] Port range: {start_port}-{end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            is_open = scan_port(host, port)

            if is_open:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
            else:
                print(f"Port {port}: CLOSED")

            time.sleep(0.1)

        except Exception as error:
            print(f"Port {port}: ERROR - {error}")

    print("\n[SCANNER] Scan complete.")

    if open_ports:
        print(f"[SCANNER] Open ports found: {open_ports}")
    else:
        print("[SCANNER] No open ports found in the specified range.")


def main():
    """Run the scanner from command-line arguments."""
    if len(sys.argv) != 4:
        print("Usage: python3 port_scanner.py <host> <start_port> <end_port>")
        print("Example: python3 port_scanner.py 127.0.0.1 20 100")
        return

    host = sys.argv[1]

    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])

        port_scanner(host, start_port, end_port)

    except ValueError as error:
        print(f"[INPUT ERROR] {error}")
    except RuntimeError as error:
        print(f"[SCAN ERROR] {error}")
    except Exception as error:
        print(f"[UNEXPECTED ERROR] {error}")


if __name__ == "__main__":
    main()