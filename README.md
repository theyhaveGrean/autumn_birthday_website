# Autumn Notes

Run on a Raspberry Pi with:

```bash
python3 server.py
```

Open `http://<raspberry-pi-ip>:8000/home.html` on the network. The home page PIN is `4008`; successful entry opens the public guestbook. Messages are stored in `guestbook.db` using SQLite, created automatically. For access outside the home network, put this behind a reverse proxy with HTTPS.
