import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("dolar.db")
filas = conn.execute("SELECT fecha, venta FROM cotizaciones ORDER BY fecha").fetchall()
conn.close()

fechas = [f[0] for f in filas]
valores = [f[1] for f in filas]

plt.plot(fechas, valores, marker="o")
plt.xticks(rotation=45)
plt.title("Evolución del dólar blue")
plt.tight_layout()
plt.savefig("grafico.png")
print("Gráfico guardado en grafico.png")
