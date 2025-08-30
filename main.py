from animales import (
    Perro, Gato, Refugio,
    Dueño, Veterinario,
    GestorAnimales
)


def main():
    # Crear dueños y refugios
    dueño1 = Dueño(nombre="Ana", direccion="Calle 123")
    refugio1 = Refugio(nombre="Refugio San Martín")

    # Crear animales
    perro = Perro(nombre="Firulais", edad=3, raza="Labrador", refugio=refugio1, cuidador=dueño1)
    gato = Gato(nombre="Michi", edad=2, color="Negro", refugio=refugio1, cuidador=dueño1)

    # Añadir animales al refugio
    refugio1.animales.extend([perro, gato])

    # Crear cuidadores adicionales
    vet = Veterinario(nombre="Carlos", especialidad="Pequeñas especies")

    # Crear gestor de animales
    gestor = GestorAnimales(
        animales=[perro, gato],
        cuidadores=[dueño1, vet]
    )

    # Revisar y cuidar
    gestor.revisar_y_cuidar()


if __name__ == "__main__":
    main()
