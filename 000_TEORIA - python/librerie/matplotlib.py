import matplotlib.pyplot as plt
import numpy as np

# 1. Creazione di Dati

# Creare dati per il grafico
x = np.linspace(0, 10, 100)  # 100 punti tra 0 e 10
y = np.sin(x)  # Funzione seno

# 2. Creazione di un Grafico Lineare

# Grafico lineare
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Seno', color='blue')
plt.title('Grafico della Funzione Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

# 3. Creazione di un Grafico a Dispersione

# Dati per un grafico a dispersione
y2 = np.cos(x)  # Funzione coseno

# Grafico a dispersione
plt.figure(figsize=(10, 5))
plt.scatter(x, y2, color='red', label='Coseno', alpha=0.5)
plt.title('Grafico a Dispersione della Funzione Coseno')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

# 4. Creazione di un Istogramma

# Dati casuali per l'istogramma
data = np.random.randn(1000)  # 1000 punti distribuiti normalmente

# Istogramma
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, color='green', alpha=0.7)
plt.title('Istogramma di Dati Casuali')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.grid(True)
plt.show()

# 5. Creazione di un Grafico a Barre

# Dati per un grafico a barre
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Grafico a barre
plt.figure(figsize=(10, 5))
plt.bar(categories, values, color='orange')
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.grid(axis='y')
plt.show()

# 6. Grafico di Contorno

# Creare dati per un grafico di contorno
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = np.sqrt(X**2 + Y**2)

# Grafico di contorno
plt.figure(figsize=(10, 5))
contour = plt.contour(X, Y, Z, levels=20)
plt.title('Grafico di Contorno')
plt.xlabel('X')
plt.ylabel('Y')
plt.clabel(contour, inline=True, fontsize=8)
plt.show()

# 7. Salvataggio di un Grafico

# Creare e salvare un grafico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Seno', color='blue')
plt.title('Grafico della Funzione Seno (Salvato)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.savefig('seno_plot.png')
print("Grafico salvato come 'seno_plot.png'.")

# 8. Grafico con Sottotitoli e Annotazioni

# Grafico con annotazione
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Seno', color='blue')
plt.title('Grafico della Funzione Seno con Annotazione')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Annotare un punto specifico
plt.annotate('Punto massimo', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
