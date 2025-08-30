from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Protocol, List, Optional


# Interfaz para cuidadores (equivalente a ICuidador)
class Cuidador(Protocol):
    def alimentar(self, animal: Animal) -> None: ...


# Implementaciones de cuidadores
class Veterinario:
    def __init__(self, nombre: str, especialidad: str) -> None:
        self._nombre = nombre
        self._especialidad = especialidad

    def alimentar(self, animal: Animal) -> None:
        print(f"[VETERINARIO {self._nombre}] Alimenta a {animal.nombre}")


class Dueño:
    def __init__(self, nombre: str, direccion: str) -> None:
        self._nombre = nombre
        self._direccion = direccion

    def alimentar(self, animal: Animal) -> None:
        print(f"[DUEÑO {self._nombre}] Cuida y alimenta a {animal.nombre}")


@dataclass
class Refugio:
    nombre: str
    animales: List["Animal"] = field(default_factory=list)


# Clase abstracta Animal
@dataclass
class Animal(ABC):
    nombre: str
    edad: int
    refugio: Optional[Refugio] = None
    cuidador: Optional[Cuidador] = None

    @abstractmethod
    def hacer_sonido(self) -> str: ...


# Subclases concretas
@dataclass
class Perro(Animal):
    raza: str = "Mestizo"

    def hacer_sonido(self) -> str:
        return "¡Guau guau!"


@dataclass
class Gato(Animal):
    color: str = "Blanco"

    def hacer_sonido(self) -> str:
        return "¡Miau!"


# Historial médico
@dataclass
class HistorialMedico:
    fecha: str
    diagnostico: str


# Logger
class Logger:
    def log(self, mensaje: str) -> None:
        print(f"[LOG] {mensaje}")


# Gestor de animales
class GestorAnimales:
    def __init__(self, animales: List[Animal], cuidadores: List[Cuidador], logger: Optional[Logger] = None) -> None:
        self._animales = animales
        self._cuidadores = cuidadores
        self._logger = logger or Logger()

    def revisar_y_cuidar(self) -> None:
        for a in self._animales:
            sonido = a.hacer_sonido()
            msg = f"El animal {a.nombre} hace un sonido: {sonido}"
            self._logger.log(msg)
            for c in self._cuidadores:
                c.alimentar(a)
