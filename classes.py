
#Preciso determinar expressao (Se)
#Preciso determinar comando (Se)

class Variable(object):
    value = []
    vectorSize = None
    def __init__(self,lineno, tipo=None ,vector =False,vectorSize = 1):
        self.tipo = tipo
        self.isVector = vector
        self.vectorSize = vectorSize
        self.lineno = lineno

    def setTipo(self,tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo

    def getLineno(self):
        return self.lineno

    def setValue(self,value, position = 0):
        if(isVector == False):
            self.value.insert(0,value)
        else:
            if position <vectorSize and position >= 0:
                self.value.insert(position,value)
            #else:
                #RETORNAR ERRO DE ACESSO EM POSIÇÃO QUE NÃO PODE!!!!

class Funcao(object):
    def __init__(self,lineno,dictVariable,arvoreBloco):
        self.dictVariable = dictVariable
        self.arvoreBloco = arvoreBloco
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

    def setTipo(self,tipo):
        self.tipo = tipo

    def getDictVariable(self):
        return self.dictVariable
    
    def getArvoreBloco(self):
        return self.arvoreBloco

#Não lembro oq é kkk######################
class BinaryOperation(object):
    def __init__(self,lineno,operation,left,right):
        self.operation = operation
        self.left = left
        self.right = right
        self.lineno = lineno

    def getOperation(self):
        return self.operation

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def getLineno(self):
        return self.lineno

class Comparative(object):
    def __init__(self,lineno,comparative,left,right):
        self.comparative = comparative
        self.left = left
        self.right = right
        self.lineno = lineno

    def getComparative(self):
        return self.comparative
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def getLineno(self):
        return self.lineno
#######################################

class Ou(object):
    def __init__(self,lineno,arvoreOu,arvoreE):
        self.arvoreOu = arvoreOu #outro objeto Ou
        self.arvoreE = arvoreE #objeto E
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class E(object):
    def __init__(self,lineno,arvoreE, arvoreEquivalete):
        self.arvoreE = arvoreE #outro objeto E
        self.arvoreEquivalete = arvoreEquivalete  # objeto Equivalete
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Equivalente(object):
    def __init__(self,lineno,arvoreEquivalente,arvoreDesigualdade,equivalencia=True):
        self.arvoreEquivalente = arvoreEquivalente #outro objeto Equivalente
        self.arvoreDesigualdade = arvoreDesigualdade #objeto Desigualdade
        self.equivalencia = equivalencia #Se a operação for a comparação ==, se for negativo é != 
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Desigualdade(object):
    def __init__(self,lineno,arvoreDesigualdade,arvoreAdicao,Maior = True,Igual = False):
        self.arvoreDesigualdade = arvoreDesigualdade #outro objeto Desigualdade
        self.arvoreAdicao = arvoreAdicao #objeto Adição
        self.Maior = Maior #Determina se a operação é >(maior) ou <(menor)
        self.Igual = Igual #Determina se a operação tem igual ( como <= ) ou não
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Adicao(object):
    def __init__(self,lineno,arvoreAdicao,arvoreMultiplicacao,Mais = True):
        self.arvoreAdicao = arvoreAdicao #Outro objeto Adicao
        self.arvoreMultiplicacao = arvoreMultiplicacao #Arvore das operações multiplicativas
        self.Mais = Mais    #Verdade se a operação for + e falso se a operação for -
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Multiplicacao(object):
    def __init__ (self,lineno,arvoreMultiplicacao,arvoreUnitaria,Vezes = False,Divisao = False,Resto = False):
        self.arvoreMultiplicacao = arvoreMultiplicacao
        self.arvoreUnitaria = arvoreUnitaria
        self.Vezes = Vezes
        self.Divisao = Divisao
        self.Resto = Resto
        self.lineno = lineno
        if Vezes == False and Divisao == False and Resto == False :
            print("Criando expressão de multiplicacao sem operacao!!")
            exit()

    def getLineno(self):
        return self.lineno

class Atribuicao(object):
    def __init__ (self,lineno,arvoreLval,arvoreAtribuicao):
        self.arvoreLval = arvoreLval # expressão da esquerda que recebe a atribuição
        self.arvoreAtribuicao = arvoreAtribuicao # outro objeto atribuicao
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Condicional(object):
    def __init__ (self,lineno,arvoreOu,arvoreExpressao,arvoreCondicional):
        self.arvoreOu = arvoreOu #objeto Ou
        self.arvoreExpressao = arvoreExpressao #objeto expressao
        self.arvoreCondicional = arvoreCondicional #outro objeto Condicional
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Lval(object):
    def __init__ (self,lineno,id,expressao = None):
        self.id = id #identificador da variavel
        self.expressao = expressao #Se expressao é None a variavel não é um vetor
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

#Arvore com várias expressoes separadas por vírgula
class ListExpr(object):
    def __init__ (self,lineno,arvoreListExpr,arvoreAtribuicao):
        self.arvoreListExpr = arvoreListExpr #outro objeto ListExpr
        self.arvoreAtribuicao = arvoreAtribuicao #Objeto Atribuicao
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

class Primexpr(object):
    def __init__(self,lineno,identificador = None,arvoreListExpr = None,arvoreAtribuicao = None,valorConstante = None, isFunction = False,isVariable = False,isExpression=False,isCar=False,isInt=False):
        self.identificador = identificador
        self.arvoreListExpr = arvoreListExpr
        self.arvoreAtribuicao = arvoreAtribuicao
        self.valorConstante = valorConstante
        self.isFunction = isFunction
        self.isVariable = isVariable
        self.isExpression = isExpression
        self.isCar = isCar
        self.isInt = isInt
        self.lineno = lineno
        #Talvez seja interessante fazer algumas verificações para garantir que tudo foi colocado certinho nesse objeto

    def getLineno(self):
        return self.lineno

class UnaryExpr(object):
    def __init__(self,lineno,isNegativo=False,isMenos=False):
        self.isNegativo = isNegativo
        self.isMenos = isMenos
        self.lineno = lineno
        if(isMenos == False and isNegativo == False):
            print("Classe unária sem operacao")
            exit()

    def getLineno(self):
        return self.lineno

class ListComando(object):
    def __init__(self,lineno,arvoreComando , arvoreListaComando = None):
        self.arvoreComando = arvoreComando #Objeto comando
        self.arvoreListaComando = arvoreListaComando #outro objeto ListComando ou None 
        self.lineno = lineno

    def getArvoreComando(self):
        return self.arvoreComando
    
    def getArvoreListComando(self):
        return self.arvoreListaComando

    def getLineno(self):
        return self.lineno
########Classes da gramática COMANDO############################
class Se(object):
    def __init__(self,lineno,expressao,comando,senao=False,comandosenao = None):
        self.expressao = expressao
        self.comando = comando
        self.senao = senao
        self.comandosenao = comandosenao
        self.lineno = lineno

    def getExpressao(self):
        return self.expressao
    
    def getComando(self):
        return self.comando
    
    def isSenao(self):
        return self.senao
    
    def getComandoSenao(self):
        return self.comandosenao

    def getLineno(self):
        return self.lineno

class Enquanto(object):
    def __init__(self,lineno,expressao,comando):
        self.expressao = expressao
        self.comando = comando
        self.lineno = lineno

    def getExpressao(self):
        return self.expressao

    def getComando(self):
        return self.comando

    def getLineno(self):
        return self.lineno

class Leia(object):
    def __init__ (self,lineno,arvoreLvalue):
        self.arvoreLvalue = arvoreLvalue
        self.lineno = lineno

    def getArvoreLvalue(self):
        return self.arvoreLvalue

    def getLineno(self):
        return self.lineno

class Escreva(object):
    #NÃO ESQUECER DE VERIFICAR O CASO DA EXPRESSAO OU CADEIA PASSADA SEREM VAZIAS!!
    def __init__ (self,lineno,value = None,isExpressao = False, isCadeiaDeCaracteres = False):
        self.value = value #Valor passado para a função escrever
        self.isExpressao = isExpressao #Caso seja uma árvore de expressão
        self.isCadeiaDeCaracteres = isCadeiaDeCaracteres #Caso seja uma cadeia de Caracteres
        self.lineno = lineno

        if isCadeiaDeCaracteres != False and isExpressao != False:
            print("Operacao de escrever com entrada ambigua")
            exit()
    def getValue(self):
        return self.value
    def isExpressao(self):
        return self.isExpressao
    def isCadeiaDeCaracteres(self):
        return self.isCadeiadeCaracteres
    def getLineno(self):
        return self.lineno

#Criando um objeto sem variaveis kkk
class NovaLinha(object):
    def __init__ (self):
        pass

class Retorne(object):
    def __init__(self,lineno,expressao):
        self.expressao = expressao
        self.lineno = lineno

    def getExpressao(self):
        return self.expressao

    def getLineno(self):
        return self.lineno

################################################

class Bloco(object):
    def __init__ (self,lineno,dictVar,arvoreListaComando = None,):
        self.dictVar = dictVar
        self.arvoreListaComando = arvoreListaComando
        self.lineno = lineno

    def getDictVar(self):
        return self.dictVar
    def getArvoreListComando(self):
        return self.arvoreListaComando

    def getLineno(self):
        return self.lineno

#classe do escopo de variáveis
#Para determinar os pais , manter uma lista com o objeto dos filhos subindo e depois quando encontrar o pai, setar o pai nos filhos e limpar a lista
escopo = {}
class Scope:
    def __init__(self,variableDict,parent=None):
        self.variableDict = variableDict 
        self.parent = parent
    
    def getVariableDict(self):
        return self.variableDict
    def getParent(self):
        return self.parent

#Fábrica para criar a estrutura dos escopos
def createScope(variableDict,parent):
    global escopo
    newScope = Scope(variableDict,parent)
    if parent == None:
        escopo["global"] = newScope.__dict__
    else:
        escopo[id(newScope)] = newScope.__dict__
    return newScope

####### Para percorrer a árvore#######


def walkTreeScopeStart(Tree,parent = None):
    localVariables = {}
    global escopo
    for x in Tree:
        if isinstance(Tree[x] , Variable):
            localVariables[x] = Tree[x]

        elif isinstance(Tree[x], Funcao):    
            walkTreeScopeFunction(Tree[x],"global")
            pass

    x = createScope(localVariables,None)
    #print(x)
    #print(escopo)

def walkTreeScopeFunction(Tree,parent):
    x = Tree.getArvoreBloco()

    if x != None: 
        walkTreeScopeBloco(x,parent,Tree.getDictVariable())
    


def walkTreeScopeBloco(Tree,parent,functionVariablesDict = None):
    localVariables = Tree.getDictVar()

    if functionVariablesDict != None:
        repetido = False
        for x in functionVariablesDict:
            if x in localVariables:
                repetido = True
        if repetido == True:
            print("Erro na linha "+Tree.getLineno()+ ": variavel " + "já foi declarada")
            exit()
        localVariables.update(functionVariablesDict)
    
    newParent = createScope(localVariables,parent)

    print(id(newParent))

    listcomando = Tree.getArvoreListComando()
    
    if listcomando != None:
        walkTreeScopeListComando(listcomando,newParent)

def walkTreeScopeListComando(Tree,parent):
    
    newTree = Tree.getArvoreListComando()
    comando = Tree.getArvoreComando()

    if comando != None:
        walkTreeScopeComando(comando,parent)

    if newTree != None:
        walkTreeScopeListComando(newTree,parent)
    

def walkTreeScopeComando(Tree,parent):
    #print(Tree)

    if isinstance(Tree, Se):
        comandoSe = Tree.getComando()
        comandoSenao = Tree.getComandoSenao()
        
        if comandoSe != None:
            walkTreeScopeComando(comandoSe,parent)
        if comandoSenao != None:
            walkTreeScopeComando(comandoSenao,parent)

    elif isinstance(Tree, Enquanto ):
        comando = Tree.getComando()

        if comando != None:
            walkTreeScopeComando(comando,parent)
    
    elif isinstance(Tree,Leia):
        pass
    
    elif isinstance(Tree, Escreva):
        pass
    
    elif isinstance(Tree,NovaLinha):
        pass
    
    elif isinstance(Tree, Retorne):
        pass
    
    elif isinstance(Tree, Bloco):
        walkTreeScopeBloco(Tree,parent)
    pass







