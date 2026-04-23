# CYB333 Security Automation Midterm

## Overview
This project demonstrates a basic client-server socket connection and a Python-based port scanner.

## Files
- `server.py` – Server script that listens for connections
- `client.py` – Client script that connects to the server and exchanges messages
- `port_scanner.py` – Scans a range of ports on approved hosts

## How to Run

### Start Server
```bash
python3 server.py

### Start Client
```bash
python3 client.py

python3 port_scanner.py 127.0.0.1 20 100
python3 port_scanner.py 127.0.0.1 65430 65435
python3 port_scanner.py scanme.nmap.org 20 100

#### Ethical Notice
This scanner is restricted to:
- localhost (127.0.0.1)
- scanme.nmap.org
Scanning unauthorized systems is illegal and was not performed in this project.
