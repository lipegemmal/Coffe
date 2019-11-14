
#Preciso determinar expressao (Se)
#Preciso determinar comando (Se)

class Variable(object):
    value = []
    vectorSize = None
    def __init__(self, tipo=None ,vector =False,vectorSize = 1):
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

#Não lembro oq é kkk######################
class BinaryOperation(object):
    def __init__(self,operation,left,right):
        self.operation = operation
        self.left = left
        self.right = right

    def getOperation(self):
        return self.operation

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

class Comparative(object):
    def __init__(self,comparative,left,right):
        self.comparative = comparative
        self.left = left
        self.right = right
    
    def getComparative(self):
        return self.comparative
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
#######################################

class Ou(object):
    def __init__(self,arvoreOu,arvoreE):
        self.arvoreOu = arvoreOu #outro objeto Ou
        self.arvoreE = arvoreE #objeto E

class E(object):
    def __init__(self, arvoreE, arvoreEquivalete):
        self.arvoreE = arvoreE #outro objeto E
        self.arvoreEquivalete = arvoreEquivalete  # objeto Equivalete

class Equivalente(object):
    def __init__(self,arvoreEquivalente,arvoreDesigualdade,equivalencia=True):
        self.arvoreEquivalente = arvoreEquivalente #outro objeto Equivalente
        self.arvoreDesigualdade = arvoreDesigualdade #objeto Desigualdade
        self.equivalencia = equivalencia #Se a operação for a comparação ==, se for negativo é != 

class Desigualdade(object):
    def __init__(self,arvoreDesigualdade,arvoreAdicao,Maior = True,Igual = False):
        self.arvoreDesigualdade = arvoreDesigualdade #outro objeto Desigualdade
        self.arvoreAdicao = arvoreAdicao #objeto Adição
        self.Maior = Maior #Determina se a operação é >(maior) ou <(menor)
        self.Igual = Igual #Determina se a operação tem igual ( como <= ) ou não

class Adicao(object):
    def __init__(self,arvoreAdicao,arvoreMultiplicacao,Mais = True):
        self.arvoreAdicao = arvoreAdicao #Outro objeto Adicao
        self.arvoreMultiplicacao = arvoreMultiplicacao #Arvore das operações multiplicativas
        self.Mais = Mais    #Verdade se a operação for + e falso se a operação for -

class Multiplicacao(object):
    def __init__ (self,arvoreMultiplicacao,arvoreUnitaria,Vezes = False,Divisao = False,Resto = False):
        self.arvoreMultiplicacao = arvoreMultiplicacao
        self.arvoreUnitaria = arvoreUnitaria
        self.Vezes = Vezes
        self.Divisao = Divisao
        self.Resto = Resto
        if Vezes == False and Divisao == False and Resto == False :
            print("Criando expressão de multiplicacao sem operacao!!")
            exit()

class Atribuicao(object):
    def __init__ (self,arvoreLval,arvoreAtribuicao):
        self.arvoreLval = arvoreLval # expressão da esquerda que recebe a atribuição
        self.arvoreAtribuicao = arvoreAtribuicao # outro objeto atribuicao

class Condicional(object):
    def __init__ (self,arvoreOu,arvoreExpressao,arvoreCondicional):
        self.arvoreOu = arvoreOu #objeto Ou
        self.arvoreExpressao = arvoreExpressao #objeto expressao
        self.arvoreCondicional = arvoreCondicional #outro objeto Condicional

class Lval(object):
    def __init__ (self,id,expressao = None):
        self.id = id #identificador da variavel
        self.expressao = expressao #Se expressao é None a variavel não é um vetor

#Arvore com várias expressoes separadas por vírgula
class ListExpr(object):
    def __init__ (self,arvoreListExpr,arvoreAtribuicao):
        self.arvoreListExpr = arvoreListExpr #outro objeto ListExpr
        self.arvoreAtribuicao = arvoreAtribuicao #Objeto Atribuicao

class Primexpr(object):
    def __init__(self,identificador = None,arvoreListExpr = None,arvoreAtribuicao = None,valorConstante = None, isFunction = False,isVariable = False,isExpression=False,isCar=False,isInt=False):
        self.identificador = identificador
        self.arvoreListExpr = arvoreListExpr
        self.arvoreAtribuicao = arvoreAtribuicao
        self.valorConstante = valorConstante
        self.isFunction = isFunction
        self.isVariable = isVariable
        self.isExpression = isExpression
        self.isCar = isCar
        self.isInt = isInt
        #Talvez seja interessante fazer algumas verificações para garantir que tudo foi colocado certinho nesse objeto


class Se(object):
    def __init__(self,expressao,comando,senao=False,comandosenao = None):
        self.expressao = expressao
        self.comando = comando
        self.senao = senao
        if(senao != False):
            self.comandosenao = comandosenao
        
class Enquanto(object):
    def __init__(self,expressao,comando):
        self.expressao = expressao
        self.comando = comando

#classe do escopo de variáveis
#Para determinar os pais , manter uma lista com o objeto dos filhos subindo e depois quando encontrar o pai, setar o pai nos filhos e limpar a lista
escopo = {}
class Scope:
    def __init__(self,variableDict,parent=None):
        self.variableDict = variableDict 
        self.parent = parent

#Fábrica para criar a estrutura dos escopos
def createScope(variableDict,parent):
    global escopo
    newScope = Scope(variableDict,parent)
    if parent == None:
        escopo["global"] = newScope.__dict__
    else:
        escopo[id(newScope)] = newScope.__dict__
    return newScope
