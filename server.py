import socket

HOST = "127.0.0.1"
PORT =65432

def start_server():
    """Start the server and wait for one client connection."""
    try: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind ((HOST, PORT))
            server_socket.listen(1)
        
            print(f"[SERVER] Listening on {HOST}:{PORT}...")
       
            conn, addr = server_socket.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")

                while True:
                    data = conn.recv(1024)

                    if not data:
                        print("[SERVER] Client disconnected cleanly.")
                        break
                    
                    message = data.decode("utf-8")
                    print(f"[SERVER] Recieved: {message}")

                    response = f"Server received: {message}"
                    conn.sendall(response.encode("utf-8"))
                    print(f"[SERVER] Sent: {response}")
    
    except OSError as error:
        print(f"[SERVER ERROR] {error}")
        
    except Exception as error:
        print(f"[UNEXPECTED SERVER ERROR] {error}")

if __name__ == "__main__":
    start_server()