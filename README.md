# Autumn Notes

## GitHub Pages

This project works as a static GitHub Pages site. Set GitHub Pages to deploy from the `main` branch, then open the root page. The frontend uses Supabase's public REST API. Run `supabase.sql` once in the Supabase SQL Editor.

The root page uses a retro green terminal theme and does not request prior messages until PIN `4008` is entered. This is a privacy gate, not strong authentication: GitHub Pages exposes the PIN and publishable API key to anyone inspecting the site. For real security, move PIN validation and database reads behind a server-side authenticated endpoint and remove anonymous `select` access from Supabase RLS.

For a truly shared public database, deploy `server.py` to a Raspberry Pi or another hosting service and point the frontend API requests at that server.

## Optional Raspberry Pi server

Run with:

```bash
python3 server.py
```

Open `http://<raspberry-pi-ip>:8000/home.html` on the network. The home page PIN is `4008`; successful entry opens the public guestbook. Messages are stored in `guestbook.db` using SQLite, created automatically. For access outside the home network, put this behind a reverse proxy with HTTPS.
