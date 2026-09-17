#!/usr/bin/env python3
"""
codebase/server.py
Máy chủ HTTP cục bộ phục vụ giao diện Prototype và cầu nối API AI thời gian thực
Nhóm Phronesis - E403 - Hackathon AI20K Batch 04

Chạy:
    python3 codebase/server.py
Truy cập:
    http://localhost:8000
"""

import os
import sys
import json
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from codebase.triage_engine import analyze_message

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CODEBASE_DIR = os.path.join(ROOT_DIR, "codebase")
GOLDEN_SET_PATH = os.path.join(ROOT_DIR, "eval", "golden_set.json")

class PhronesisHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CODEBASE_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "/index.html"
            return super().do_GET()
        elif self.path == "/api/golden-set":
            if os.path.exists(GOLDEN_SET_PATH):
                with open(GOLDEN_SET_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
            else:
                self.send_error(404, "Golden set not found")
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/triage":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body)
                content = data.get("content", "")
                author = data.get("author", "WebUser")
                msg_id = data.get("msg_id", f"WEB_{int(time.time()*1000)}")

                start_t = time.time()
                result = analyze_message(content, author=author, msg_id=msg_id)
                elapsed = round(time.time() - start_t, 3)

                response_payload = {
                    "status": "success",
                    "latency_sec": elapsed,
                    "msg_id": msg_id,
                    "decision": result
                }

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(response_payload, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
            return
        
        self.send_error(404, "Endpoint not found")

def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, PhronesisHandler)
    print("=" * 65)
    print(f"🚀 Phronesis Live Prototype Server đang chạy tại: http://localhost:{port}")
    print(f"📡 API Triage Live Endpoint: POST http://localhost:{port}/api/triage")
    print(f"📦 Golden Set Endpoint:      GET  http://localhost:{port}/api/golden-set")
    print("Nhấn Ctrl+C để dừng máy chủ.")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Đã tắt máy chủ.")
        httpd.server_close()

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port)
