# Autumn Notes

## GitHub Pages

This project works as a static GitHub Pages site. Set GitHub Pages to deploy from the `main` branch, then open `/home.html` as the PIN landing page. On GitHub Pages, notes are stored in the visitor's browser with `localStorage` because GitHub Pages cannot run a server or accept database writes. That means notes are not shared between visitors.

For a truly shared public database, deploy `server.py` to a Raspberry Pi or another hosting service and point the frontend API requests at that server.

## Optional Raspberry Pi server

Run with:

```bash
python3 server.py
```

Open `http://<raspberry-pi-ip>:8000/home.html` on the network. The home page PIN is `4008`; successful entry opens the public guestbook. Messages are stored in `guestbook.db` using SQLite, created automatically. For access outside the home network, put this behind a reverse proxy with HTTPS.
