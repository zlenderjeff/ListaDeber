class Metodos():
    def ingreso(self,lista,tamano):
        i=0
        while(i<tamano):
            print("Ingrese el [",i,"] valor de la lista")
            numero=int(input("numero "))
            lista.append(numero)
            i=i+1
    def impresion(self,lista,tamano):
        for i in range(tamano):
            print(lista[i])
    def agregarUltimo(self,lista,itm):
        lista.append(itm)
    def vaciarLista(self,lista):
        lista.clear()
    def unirListas(self,lista1,lista2):
        lista1.extend(lista2)
    def contarElemento(self, lista, elemento):
        count = lista.count(elemento)
        return count
    def indiceElemento(self,lista,elemento):
        indice = lista.index(elemento)
        return indice
    def insertarElemento(self,lista,index,elemento):
        lista.insert(index,elemento)
    def extraerElemento(self,lista,index):
        lista.pop(index)
    def remover(self,lista,elemento):
        lista.remove(elemento)
    def invertir(self,listas):
        listas.reverse()
    def ordenar(self,listas):
        listas.sort()
    def limpiar(self,listas):
        listas.clear()


    
