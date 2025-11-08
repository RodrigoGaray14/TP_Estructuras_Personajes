class Personaje:
    """
    Clase que modela un Personaje de Ciencia Ficción.
    Se aplica encapsulamiento usando el prefijo '_' para atributos internos.
    """
    def __init__(self,nombre, especie, planeta, nivel_poder):
        self._nombre = nombre
        self._epecie = especie
        self._planeta = planeta
        self._nivel_poder = nivel_poder #nivel base de poder
        
    # Inventario (usaremos una lista simple por ahora)
        self._inventario = []
        
    # Habilidades (usaremos un conjunto o 'set' para asegurar que sean únicas)
        self._habilidades = set() 
        
    # 3. Componentes para Poder Recursivo 
        # Aquí guardaremos objetos o personajes que 'componen' el poder total 
        self._componentes_poder = []       
        
    #---------------------------

    # --- MÉTODOS GETTERS (Para obtener datos) ---
    
    def obtener_nombre(self):
        """Devuelve el nombre del personaje."""
        return self._nombre

    def obtener_nivel_poder_base(self):
        """Devuelve el nivel de poder base (sin componentes recursivos)."""
        return self._nivel_poder

    def obtener_inventario(self):
        """Devuelve una copia del inventario."""
        # Devolvemos una copia (lista) para proteger la lista interna
        return list(self._inventario) 
    
    # --- MÉTODOS SETTERS (Para modificar datos de forma controlada) ---

    def establecer_nivel_poder_base(self, nuevo_poder):
        """Modifica el poder base, asegurando que el valor sea válido."""
        if nuevo_poder >= 0:
            self._nivel_poder = nuevo_poder
            print(f"El nivel de poder base de {self._nombre} ha sido ajustado a {nuevo_poder}.")
            return True
        print("Error: El nivel de poder debe ser no negativo.")
        return False  
    
    def agregar_objeto(self, objeto):
        """Agrega un objeto a la lista del inventario."""
        self._inventario.append(objeto)
        print(f"-> {self._nombre} ha añadido {objeto} al inventario.")

    def eliminar_objeto(self, objeto):
        """Elimina un objeto específico del inventario."""
        try:
            self._inventario.remove(objeto)
            print(f"-> {self._nombre} ha usado/eliminado {objeto}.")
            return True
        except ValueError:
            print(f"-> Error: {objeto} no se encuentra en el inventario de {self._nombre}.")
            return False
            
    def agregar_habilidad(self, habilidad):
        """Agrega una habilidad al conjunto (set), solo si no la tiene ya."""
        if habilidad not in self._habilidades:
            self._habilidades.add(habilidad)
            print(f"-> {self._nombre} ha aprendido la habilidad: {habilidad}.")
            return True
        print(f"-> {self._nombre} ya conoce la habilidad: {habilidad}.")
        return False
        
    def obtener_habilidades(self):
        return list(self._habilidades)

    # --- FUNCIÓN RECURSIVA PARA EL PODER TOTAL (REQUISITO CLAVE) ---

    def agregar_componente_poder(self, componente):
        """Añade un objeto (como otra GemaPoder o Personaje) que suma poder."""
        self._componentes_poder.append(componente)

    def calcular_poder_total(self):
        """
        Calcula el poder total de forma recursiva.
        Es la suma del poder base más el poder de sus componentes.
        """
        poder_actual = self._nivel_poder
        
        # Caso Recursivo: Recorrer los componentes y sumar su poder
        for componente in self._componentes_poder:
            # Llama al mismo método calcular_poder_total() de cada componente.
            # Esto es la recursividad y polimorfismo en acción.
            try:
                poder_actual += componente.calcular_poder_total()
            except AttributeError:
                # Caso de seguridad si el componente no tiene el método (ej: es un número)
                if isinstance(componente, (int, float)):
                    poder_actual += componente
                
        # Caso Base: Si la lista de componentes está vacía, devuelve solo el poder base.
        return poder_actual

class GemaPoder:
    """Clase auxiliar para simular un componente de poder que no es un personaje."""
    def __init__(self, nombre, poder_adicional):
        self._nombre = nombre
        self._poder = poder_adicional
    
    def obtener_nombre(self):
        return self._nombre
        
    def calcular_poder_total(self):
        """Método simple que devuelve su valor de poder para la suma recursiva."""
        return self._poder    