# Archivo: main.py

# Importamos las clases Personaje y GemaPoder del módulo (archivo) personaje.py
from personaje import Personaje, GemaPoder

def ejecutar_pruebas():
    
    # 1. CREACIÓN DE INSTANCIAS (Objetos)
    
    # Heroe: Nivel 100
    heroe = Personaje("Astro", "Humano", "Tierra", 100)
    
    # Villano: Nivel 250
    villano = Personaje("Lord Krell", "Kryllon", "Xylos", 250)
    
    # Componentes de poder extra
    gema_roja = GemaPoder("Gema de Fuerza", 50)
    gema_azul = GemaPoder("Gema de Velocidad", 80)

    print("--- ⚔️ INICIO DE PRUEBAS DE ENCAPSULAMIENTO Y ESTRUCTURAS ---")
    
    # 2. PRUEBAS DE INTERFACES (Inventario y Habilidades)
    
    heroe.agregar_objeto("Espada Láser")
    heroe.agregar_habilidad("Vuelo")
    heroe.agregar_habilidad("Vuelo") # Intenta agregarla de nuevo (el set lo evita)
    heroe.eliminar_objeto("Espada Láser")
    
    print(f"\nInventario final de {heroe.obtener_nombre()}: {heroe.obtener_inventario()}")
    print(f"Habilidades de {heroe.obtener_nombre()}: {heroe.obtener_habilidades()}")
    
    # 3. PRUEBA DE SETTER Y ENCAPSULAMIENTO
    print(f"\nPoder base inicial de {villano.obtener_nombre()}: {villano.obtener_nivel_poder_base()}")
    villano.establecer_nivel_poder_base(-100) # Prueba de validación del Setter (falla)
    villano.establecer_nivel_poder_base(300)  # Prueba de Setter (éxito)
    
    # 4. PRUEBA DE RECURSIVIDAD DE PODER
    print("\n--- 💥 PRUEBA DE CÁLCULO DE PODER RECURSIVO ---")
    
    # El héroe agrega las gemas como componentes
    heroe.agregar_componente_poder(gema_roja)
    heroe.agregar_componente_poder(gema_azul)
    
    # El villano se fusiona con el héroe (o lo atrapa) como componente
    villano.agregar_componente_poder(heroe)

    # El héroe calcula su propio poder (100 base + 50 gema_roja + 80 gema_azul)
    heroe_poder_total = heroe.calcular_poder_total()
    print(f"El poder TOTAL de {heroe.obtener_nombre()} es: {heroe_poder_total}") 
    # Debería ser: 100 + 50 + 80 = 230
    
    # El villano calcula su poder (300 base + 230 del héroe)
    villano_poder_total = villano.calcular_poder_total()
    print(f"El poder TOTAL de {villano.obtener_nombre()} es: {villano_poder_total}") 
    # Debería ser: 300 + 230 = 530

if __name__ == "__main__":
    ejecutar_pruebas()