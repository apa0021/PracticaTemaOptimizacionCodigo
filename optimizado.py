class optimizadoclass:
    array=[]
    def arrayNumeros(self):
        return self.array
    def inp():
        numero = int(input("Introduzca un numero"))
        return numero
    def add(self, n):
        self.array.append(n)
    def media(self):
        suma=0
        for n in self.array:
            suma+=n
            m=suma/len(self.array)
        return m
