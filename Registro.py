# 📚 Gestión de Libros
# > Registro completo de cada libro (título, autor, año, categoría/género, precio de venta)

# ■ S - Principio de Responsabilidad Única = Single Responsibility Principle (SRP)

# ■ Una clase debe tener una sola razón para cambiar.
# ■ Separar responsabilidades evita que los cambios en una parte del sistema afecten otras partes innecesariamente.


# Clase Libro
class Libro :
  def __init__(self, titulo, autor, año, categoria, precio):
    self.titulo = titulo
    self.autor = autor
    self.año = año
    self.categoria = categoria
    self.precio = precio
    
  def mostrar_libros(self):
    return (
      f'Título: {self.titulo}\n'
      f'Autor: {self.autor}\n'
      f'Año: {self.año}\n'
      f'Categoría: {self.categoria}\n'
      f'Precio: Q{self.precio}\n'
    )
    
    
# Clase Registro
class Registro :
  
  def __init__(self):
    # Diccionario para almacenar los libros
    self.libro = {}
  
  def Agregar_libro(self):
    print('\n\n\t-------- Bienvenido al Registro de Libros --------')
    print()
    
    while True :
      titulo = input('Ingrese el título del libro o escriba fin : ')
      
      # Verificar si el libro ya existe
      if titulo.lower() in self.libro:
        print('El libro ya existe en el registro.\n')
        titulo = input('Ingrese un título diferente o escriba fin : ')
        continue

      # Verificar si se desea finalizar el registro
      if titulo.lower() == 'fin':
        break

      # Agregar nuevo libro
      if titulo.lower() not in self.libro:
        autor = input('Ingrese el autor del libro : ')
        año = input('Ingrese el año de publicación : ')
        categoria = input('Ingrese la ►categoría o ►género del libro : ')
        precio = input('Ingrese el precio de venta del libro : ')
        
        self.libro[titulo.lower()] = Libro(titulo, autor, año, categoria, precio)
        print()


# Clase Mostrar
class Mostrar(Registro):
  
  def Mostrar_libro(self, Registro):
    self.Registro = Registro
    
    print('\n\t\t-------- Bienvenido a la Libreria --------')
    
    for index, lib in enumerate(self.Registro.libro.values(), start = 1):
      print(f"{index}. {'Libro'}")
      print(f"{lib.mostrar_libros()}")


# Clase Volver
class Volver(Registro):
  
  def Volver_a_menu(self, Registro):
    self.Registro = Registro

    while True:
      pregunta = input('¿Desea volver al menú principal? (si/no): ').strip().lower()
      if pregunta == 'si':
        self.Registro.Agregar_libro()
        
        # → Clase Mostrar
        imprimir = Mostrar()
        imprimir.Mostrar_libro(registrar)
        
      elif pregunta == 'no':
        print('\n\tGracias por utilizar el sistema de registro de libros.\n')
        print()
        break


# → Clase Registro
registrar = Registro()
registrar.Agregar_libro()

# → Clase Mostrar
imprimir = Mostrar()
imprimir.Mostrar_libro(registrar)

# → Clase Volver
regresar = Volver()
regresar.Volver_a_menu(registrar)


