from abc import ABC
from typing import List
class Persona(ABC):
    def __init__(self, nombre: str, cedula: int) -> None:
        self._cedula= cedula
        self._nombre= nombre
    
    def __repr__(self) -> str:
        return f'{self.__.__name}({self._cedula}), ({self._nombre!r})'
class Autor(Persona):
    def __init__(self, nombre: str, cedula: int) -> None:
        super().__init__(nombre, cedula)
        self.__libros: List["Libro"]=[]

