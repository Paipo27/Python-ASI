from ClaseVertice import Vertice

class Grafo:
    def _init_(self):
        self.listaVertices = {}
        self.numVertices = 0 
        
    def agregarVertice(self,clave):
        self.numVertices=self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave]= nuevoVertice
        return nuevoVertice
    
    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
    
    def _contains_(self,n):
        return n in self.listaVertices
    
    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        
    def obtenerVertices(self):
        return self.listaVertices.keys()
    
    def _iter_(self):
        return iter(self.listaVertices.values())