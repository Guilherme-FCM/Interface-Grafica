from tkinter import *

class InterfaceGrafica:
    def __init__(self, titulo = 'Interface Gráfica', dimensoes = '300x500'):
        self.__container = Tk()
        self.__container.title(titulo)
        self.__container.geometry(dimensoes)

        self.__body = self.createFrame(self.__container)
        self.__listaElementos = []

    def start(self): 
        self.packElements()
        self.__container.mainloop()

    def packElements(self, **configs):
        for elemento in self.__listaElementos: elemento.pack(configs)
        self.__listaElementos = []

    def setDimensao(self, dimensoes): self.__container.geometry(dimensoes)
    def setTitulo(self, titulo): self.__container.title(titulo)

    def addElemento(self, elemento): self.__listaElementos.append(elemento)
    def insertElemento(self, elemento, index): self.__listaElementos.insert(index, elemento)
    def removerElemento(self, elemento): self.__listaElementos.append(elemento)

    def createFrame(self, container = None, **configs): 
        frame = Frame(container if container != None else self.__body)
        frame.pack(configs)
        return frame

    def createEntry(self, container = None): return Entry(
        container if container != None else self.__body
    )
    def createLabel(self, container = None, **configs): return Label(
        container if container != None else self.__body, configs
    )
    def createButton(self, container = None, **configs): return Button(
        container if container != None else self.__body, configs
    )

    def addEntry(self, container = None): self.addElemento(self.createEntry(container))
    def addLabel(self, container = None, **configs): self.addElemento(self.createLabel(container, **configs))
    def addButton(self, container = None, **configs): self.addElemento(self.createButton(container, **configs))

    def createMenuBar(self):
        self.__menuBar = Menu(self.__container)
        self.__container.config( menu = self.__menuBar )

    def addCascateMenuBar(self, **configs): 
        self.__menuBar.add_cascade(**configs)

    def addMenu(self):
        if self.__menuBar: return Menu(self.__menuBar)
        else: 
            self.createMenuBar()
            self.addMenu()

    def destroyAll(self): 
        self.destroyBody()
        self.destroyMenu()

    def destroyBody(self): 
        self.__body.destroy()
        self.__body = self.createFrame(self.__container)

    def destroyMenu(self): self.__menuBar.destroy()