"""
demo_server.py
==============
Launches the Insider Threat Detection demo on the local network so any
device on the same Wi-Fi / LAN can open the dashboard in a browser.

Usage
-----
    python demo_server.py              # default port 5000
    python demo_server.py --port 8080  # custom port

Demo credentials
----------------
    Admin  : username=aayush  password=aayushadminpass
    Analyst: username=priya   password=analystpass
    User   : username=amit    password=amitpass

API endpoints
-------------
    http://<ip>:<port>/api/v1/risk     – JSON risk scores for all users
    http://<ip>:<port>/api/v1/threats  – threat trend data
"""
import argparse
import socket
import sys
import os

# Ensure the project root is on sys.path so `src` is importable
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.app import app  # noqa: E402  (import after path setup)


def get_lan_ip() -> str:
    """Best-effort: return this machine's LAN IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Insider Threat Detection demo server."
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=5000,
        help="TCP port to listen on (default: 5000)",
    )
    parser.add_argument(
        "--no-reloader",
        action="store_true",
        help="Disable Flask's auto-reloader (useful on some networks)",
    )
    args = parser.parse_args()

    lan_ip = get_lan_ip()
    port   = args.port

    banner = f"""
╔══════════════════════════════════════════════════════════╗
║        INSIDER THREAT DETECTION  –  DEMO SERVER          ║
╠══════════════════════════════════════════════════════════╣
║  Local  :  http://127.0.0.1:{port:<5}                    ║
║  Network:  http://{lan_ip:<15}:{port:<5}                 ║
╠══════════════════════════════════════════════════════════╣
║  Demo Credentials                                        ║
║    Admin  :  aayush  /  aayushpass                       ║
║    Analyst:  priya   /  analystpass                      ║
║    User   :  amit    /  amitpass                         ║
╠══════════════════════════════════════════════════════════╣
║  API Endpoints                                           ║
║    /api/v1/risk      – live risk scores (JSON)           ║
║    /api/v1/threats   – threat trend data (JSON)          ║
╠══════════════════════════════════════════════════════════╣
║  Press  Ctrl+C  to stop the server                       ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,           # keep debug off for demo stability
        use_reloader=not args.no_reloader,
    )


if __name__ == "__main__":
    main()
