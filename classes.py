class Variable(object):
    value = []
    vectorSize = None
    def __init__(self, tipo=None ,vector = False,vectorSize = 1):
        self.tipo = tipo
        self.isVector = vector
        self.vectorSize = vectorSize

    def setTipo(self,tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo

    def setValue(self,value, position = 0):
        if(isVector == False):
            self.value.insert(0,value)
        else:
            if position <vectorSize and position >= 0:
                self.value.insert(position,value)
            #else:
                #RETORNAR ERRO DE ACESSO EM POSIÇÃO QUE NÃO PODE!!!!