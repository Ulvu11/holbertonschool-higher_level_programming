import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Bu bizim server-imizdir.
    BaseHTTPRequestHandler - hazir server sinifidir, biz onu genislendirik.
    """

    def do_GET(self):
        """
        Bu metod GET sorgusu gelende isleyir.
        Brauzer hər URL-e girende GET sorgusu gonderir.
        self.path - istifadecinin daxil etdiyi URL-dir (/data, /status ve s.)
        """

        if self.path == "/":
            # --- ENDPOINT 1: Ana sehife ---
            # Sadece metn gonderirik
            self.send_response(200)               # Status code: 200 = ugurlu
            self.send_header("Content-type", "text/plain")  # cavab metndir
            self.end_headers()                    # basliqlari bitiririk
            self.wfile.write(b"Hello, this is a simple API!")  # cavabi yaziriq
            # b"..." - bytes formatinda metn demekdir, server bunu teler

        elif self.path == "/data":
            # --- ENDPOINT 2: JSON data ---
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)          # dict-i JSON metnine ceviririk

            self.send_response(200)
            self.send_header("Content-type", "application/json")  # cavab JSON-dur
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))  # JSON-u gonderirik

        elif self.path == "/status":
            # --- ENDPOINT 3: Status yoxlama ---
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # --- ENDPOINT 4: Namelum URL - 404 xetasi ---
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Serveri ishe saliruq
if __name__ == "__main__":
    PORT = 8000
    server = http.server.HTTPServer(("", PORT), SimpleAPIHandler)
    # ("", PORT) - butun IP-lerden gelen sorqulari dinle, PORT-da
    print(f"Server is running on http://localhost:{PORT}")
    print("Press CTRL+C to stop the server")
    server.serve_forever()  # server daima ishlemeye devam edir
