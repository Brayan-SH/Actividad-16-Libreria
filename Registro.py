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
      f'Precio: Q{self.precio}\n'
    )
    
class Registro :  
  def __init__(self):
    # Diccionario para almacenar los libros
    self.libro = {}
  
  def agregar_libro(self):
    print('\n\t-------- Bienvenido al Registro de Libros --------')
    
    
    while True :
      titulo = input('Ingrese el título del libro > fin : ')
      
      # Verificar si el libro ya existe
      if titulo.lower() in self.libro:
        print('El libro ya existe en el registro.\n')
        titulo = input('Ingrese un título diferente o escriba > fin : ')
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
        
  def mostrar_libros(self):
    print('\n\t-------- Bienvenido a la Libreria --------')
    
    for index, Lib in enumerate(self.libro.values(), start = 1):
            print(f"{index}. {Lib.mostrar_libros()}")
    print()

r = Registro()
r.agregar_libro()
r.mostrar_libros()

while True :
  pregunta = input('¿Desea agregar más libros? (si/no): ').strip().lower()
  if (pregunta == 'si') :
    r.agregar_libro()
    r.mostrar_libros()
  if (pregunta == 'no') : 
    print('\n\tGracias por utilizar el sistema de registro de libros.\n')
    break