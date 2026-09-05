import json, sqlite3
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DB = 'guestbook.db'
PIN = '4008'

def init_db():
    with sqlite3.connect(DB) as db:
        db.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, name TEXT NOT NULL, message TEXT NOT NULL, created_at TEXT NOT NULL)')

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/notes':
            with sqlite3.connect(DB) as db:
                rows = db.execute('SELECT name, message, created_at FROM notes ORDER BY id DESC').fetchall()
            return self.send_json([{'name': n, 'message': m, 'created_at': d} for n, m, d in rows])
        return super().do_GET()

    def do_POST(self):
        if self.path != '/api/notes': return self.send_error(404)
        try: data = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
        except Exception: return self.send_error(400, 'Invalid JSON')
        name, message = str(data.get('name', '')).strip(), str(data.get('message', '')).strip()
        if not name or not message or len(name) > 60 or len(message) > 1000: return self.send_error(400, 'Name or message is invalid')
        with sqlite3.connect(DB) as db: db.execute('INSERT INTO notes(name,message,created_at) VALUES(?,?,?)', (name, message, datetime.now(timezone.utc).isoformat()))
        self.send_json({'ok': True}, 201)

    def send_json(self, payload, code=200):
        raw = json.dumps(payload).encode(); self.send_response(code); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(raw))); self.end_headers(); self.wfile.write(raw)

if __name__ == '__main__':
    init_db(); print('Guestbook running at http://0.0.0.0:8000 (PIN: ' + PIN + ')'); ThreadingHTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
