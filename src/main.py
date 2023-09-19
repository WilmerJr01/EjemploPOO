from person import Autor
from book import LibroImpreso, LibroDigital

def main() -> None:
    nombre= input("Digite el nombre del autor")
    cedula= int(input("Digite la cedula"))
    autor= Autor(nombre, cedula)

    print(autor)

    libro= LibroImpreso(titulo= "Cien AÑos de Soledad", isbn= "12233333", genero= "Novela", formato="Tapa Dura", valor=80000.0, paginas=193, num_ejemplares= 450000)
    libro2= LibroDigital(titulo= "Harry Potter", isbn= "12233377", genero= "Novela", formato="Tapa Dura", valor=50000.0, has_hipervinculo=False)

    print (libro)
if __name__ == '__main__':
    main()