# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    # Constantes
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    def __init__(self, code: str, title: str, text: str, importance: str):
        # Atributos
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()  # Fecha y hora actual
        self.tags = []  # Lista vacía por defecto
    def add_tag(self, tag: str):
        # Añadir etiqueta si no existe
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        # Formato de la cadena que se retorna
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"
