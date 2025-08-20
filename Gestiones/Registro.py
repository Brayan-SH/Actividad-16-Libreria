from diccionarioLibros import Libros

# 📚 Gestión de Libros
# > Registro completo de cada libro (título, autor, año, categoría/género, precio de venta)

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
      f'Precio: {self.precio}\n'
    )
    
class Registro :  
  def __init__(self):
    # Diccionario para almacenar los libros
    self.libros = Libros
  
  def agregar_libro(self):
    print('-------- Bienvenido al Registro de Libros --------')
    
    
    while True :
      titulo = input('Ingrese el título del libro: ')
      
      # Verificar si el libro ya existe
      if titulo.lower() in self.libros:
        print('El libro ya existe en el registro.\n')
        titulo = input('Ingrese un título diferente o escriba > fin: ')

      # Verificar si se desea finalizar el registro
      if titulo.lower() == 'fin':
        break

      # Agregar nuevo libro
      if titulo.lower() not in self.libros:
        autor = input('Ingrese el autor del libro: ')
        año = input('Ingrese el año de publicación: ')
        categoria = input('Ingrese la ►categoría o ►género del libro: ')
        precio = input('Ingrese el precio de venta del libro: ')
        
        self.libros[titulo.lower()] = Libro(autor, año, categoria, precio)
        
        for index, Libro in enumerate(self.estudiantes.values(), start = 1):
            print(f"{index}. {Libro.mostrar_info()}")
        print()
  
  