class Poligono:
    def __init__ ( self , numLados ) :
        self.numLados = numLados

    def area ( self ) :
        pass # método não implementado ; pass ignora o restante

 # subclasse de Poligono
class Quadrado ( Poligono ):
 # construtor recebe novos atributos
    def __init__ ( self , numLados , tamanhoLado ) :
 # chama o construtor da superclasse
        Poligono.__init__ ( self , numLados )
        self.tamanhoLado = tamanhoLado
        self.area_quadrado = self.area()
 # define o método area para um quadrado
    def area ( self ) :
        return self.tamanhoLado * self.tamanhoLado

class Retangulo(Poligono):
    def __init__ ( self , numLados , base , altura ) :
 # chama o construtor da superclasse
        Poligono.__init__ ( self , numLados )
        self.base = base
        self.altura = altura
 # implementa o metodo para o triangulo
    def area ( self ):
        return ( self.base * self.altura )

# triangulo é subclasse de Poligono
class Triangulo ( Poligono ):
# atributos de triangulo (base , altura )
 def __init__ ( self , numLados , base , altura ) :
 # chama o construtor da superclasse
    Poligono.__init__ ( self , numLados )
    self.base = base
    self.altura = altura
 # implementa o metodo para o triangulo
 def area ( self ):
    return ( self.base * self.altura ) / 2

quadrado = Quadrado(4 , 2)
print ("A área do quadrado é " + str( quadrado.area () ) )
print ("O quadrado tem " + str( quadrado.numLados ) + " lados ")
triangulo = Triangulo(3 , 6 , 4)
print ("A área do triângulo é " + str( triangulo.area () ) )
print ("O triângulo tem " + str( triangulo.numLados ) + " lados ")
retangulo = Retangulo(2 , 6 , 4)
print ("A área do retangulo é " + str( retangulo.area () ) )
print ("O retangulo tem " + str( retangulo.numLados ) + " lados ")