import requests, sqlite3, datetime

conn = sqlite3.connect("dolar.db")
conn.execute("""CREATE TABLE IF NOT EXISTS cotizaciones (
    fecha TEXT, compra REAL, venta REAL
)""")

r = requests.get("https://dolarapi.com/v1/dolares/blue")
r.raise_for_status()
data = r.json()

conn.execute(
    "INSERT INTO cotizaciones VALUES (?, ?, ?)",
    (datetime.datetime.now().isoformat(), data["compra"], data["venta"])
)
conn.commit()
conn.close()

print(f"Guardado: compra {data['compra']} / venta {data['venta']}")
