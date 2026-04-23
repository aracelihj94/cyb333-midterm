import socket


HOST = "127.0.0.1"
PORT = 65432

def start_client():
    """Connect to the server, send a message, and receive a response."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            print(f"[CLIENT] Connecting to {HOST}:{PORT}...")
            client_socket.connect((HOST,PORT))
            print("[CLIENT] Connected successfully.")

            message = "Hello from the client!"
            client_socket.sendall(message.encode("utf-8"))
            print(f"[CLIENT] Sent: {message}")

            response = client_socket.recv(1024) .decode("utf-8")
            print(f"[CLIENT] Received: {response}")

            print("(CLIENT] Closing connection cleanly.")

    except ConnectionRefusedError:
        print("[CLIENT ERROR] Could not connect. Is the server running?")

    except OSError as error:
        print(f"[CLIENT ERROR] {error}")

    except Exception as error:
        print(f"[UNEXPECTED CLIENT ERROR] {error}")


if __name__ == "__main__":
    start_client()