
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

    def getTipo(self):
        return self.tipo

    def getDictVariable(self):
        return self.dictVariable
    
    def getArvoreBloco(self):
        return self.arvoreBloco


class Ou(object):
    def __init__(self,lineno,arvoreOu,arvoreE):
        self.arvoreOu = arvoreOu #outro objeto Ou
        self.arvoreE = arvoreE #objeto E
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

    def getArvoreOu(self):
        return self.arvoreOu
    
    def getArvoreE(self):
        return self.arvoreE

class E(object):
    def __init__(self,lineno,arvoreE, arvoreEquivalente):
        self.arvoreE = arvoreE #outro objeto E
        self.arvoreEquivalete = arvoreEquivalente  # objeto Equivalete
        self.lineno = lineno

    def getLineno(self):
        return self.lineno
    
    def getArvoreE(self):
        return self.arvoreE
    
    def getArvoreEquivalente(self):
        return self.arvoreEquivalente

class Equivalente(object):
    def __init__(self,lineno,arvoreEquivalente,arvoreDesigualdade,equivalencia=True):
        self.arvoreEquivalente = arvoreEquivalente #outro objeto Equivalente
        self.arvoreDesigualdade = arvoreDesigualdade #objeto Desigualdade
        self.equivalencia = equivalencia #Se a operação for a comparação ==, se for negativo é != 
        self.lineno = lineno

    def getLineno(self):
        return self.lineno
    
    def getArvoreEquivalente(self):
        return self.arvoreEquivalente
    
    def getArvoreDesigualdade(self):
        return self.arvoreDesigualdade

    def getIsEquivalencia(self):
        return self.equivalencia

class Desigualdade(object):
    def __init__(self,lineno,arvoreDesigualdade,arvoreAdicao,Maior = True,Igual = False):
        self.arvoreDesigualdade = arvoreDesigualdade #outro objeto Desigualdade
        self.arvoreAdicao = arvoreAdicao #objeto Adição
        self.Maior = Maior #Determina se a operação é >(maior) ou <(menor)
        self.Igual = Igual #Determina se a operação tem igual ( como <= ) ou não
        self.lineno = lineno

    def getLineno(self):
        return self.lineno
    
    def getArvoreDesigualdade(self):
        return self.arvoreDesigualdade
    
    def getArvoreAdicao(self):
        return self.arvoreAdicao
    
    def getIsMaior(self):
        return self.Maior
    
    def getIsIgual(self):
        return self.Igual

class Adicao(object):
    def __init__(self,lineno,arvoreAdicao,arvoreMultiplicacao,Mais = True):
        self.arvoreAdicao = arvoreAdicao #Outro objeto Adicao
        self.arvoreMultiplicacao = arvoreMultiplicacao #Arvore das operações multiplicativas
        self.Mais = Mais    #Verdade se a operação for + e falso se a operação for -
        self.lineno = lineno

    def getLineno(self):
        return self.lineno
    
    def getArvoreAdicao(self):
        return self.arvoreAdicao
    
    def getArvoreMultiplicacao(self):
        return self.arvoreMultiplicacao
    
    def getIsMais(self):
        return self.Mais

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
    
    def getArvoreMultiplicacao(self):
        return self.arvoreMultiplicacao
    
    def getArvoreUnitaria(self):
        return self.arvoreUnitaria
    
    def getIsVezes(self):
        return self.Vezes
    
    def getIsDivisao(self):
        return self.Divisao
    
    def getIsResto(self):
        return self.Resto

class Atribuicao(object):
    def __init__ (self,lineno,arvoreLval,arvoreAtribuicao):
        self.arvoreLval = arvoreLval # expressão da esquerda que recebe a atribuição
        self.arvoreAtribuicao = arvoreAtribuicao # outro objeto atribuicao
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

    def getArvoreLval(self):
        return self.arvoreLval

    def getArvoreAtribuicao(self):
        return self.arvoreAtribuicao

class Condicional(object):
    def __init__ (self,lineno,arvoreOu,arvoreExpressao,arvoreCondicional):
        self.arvoreOu = arvoreOu #objeto Ou
        self.arvoreExpressao = arvoreExpressao #objeto expressao
        self.arvoreCondicional = arvoreCondicional #outro objeto Condicional
        self.lineno = lineno

    def getLineno(self):
        return self.lineno
    
    def getArvoreOu(self):
        return self.arvoreOu
    
    def getArvoreExpressao(self):
        return self.arvoreExpressao
    
    def getArvoreCondicional(self):
        return self.arvoreCondicional

class Lval(object):
    def __init__ (self,lineno,identificador,expressao = None):
        self.identificador = identificador #identificador da variavel
        self.expressao = expressao #Se expressao é None a variavel não é um vetor
        self.lineno = lineno

    def getId(self):
        return self.identificador
    
    def getExpressao(self):
        return self.expressao

    def getLineno(self):
        return self.lineno

#Arvore com várias expressoes separadas por vírgula
class ListExpr(object):
    def __init__ (self,lineno,arvoreListExpr=None,arvoreAtribuicao=None):
        self.arvoreListExpr = arvoreListExpr #outro objeto ListExpr
        self.arvoreAtribuicao = arvoreAtribuicao #Objeto Atribuicao
        self.lineno = lineno

    def getLineno(self):
        return self.lineno

    def getArvoreListExpr(self):
        return self.arvoreListExpr

    def getArvoreAtribuicao(self):
        return self.getArvoreAtribuicao


class PrimExpr(object):
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

    def getIdentificador(self):
        return self.identificador
    
    def getArvoreListExpr(self):
        return self.arvoreListExpr
    
    def getArvoreAtribuicao(self):
        return self.arvoreAtribuicao
    
    def getValorConstante(self):
        return self.valorConstante

    def getIsFunction(self):
        return self.isFunction 
    
    def getIsVariable(self):
        return self.isVariable
    
    def getIsExpression(self):
        return self.isExpression
    
    def getIsCar(self):
        return self.isCar

    def getIsInt(self):
        return self.isInt

class UnaryExpr(object):
    def __init__(self,lineno,arvorePrimExpr,isNegativo=False,isMenos=False):
        self.isNegativo = isNegativo
        self.isMenos = isMenos
        self.lineno = lineno
        self.arvorePrimExpr = arvorePrimExpr
        if(isMenos == False and isNegativo == False):
            print("Classe unária sem operacao")
            exit()

    def getLineno(self):
        return self.lineno

    def getArvorePrimExpr(self):
        return self.arvorePrimExpr

    def getIsNegativo(self):
        return self.isNegativo

    def getIsMenos(self):
        return self.isMenos


    

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
    
    def getIsSenao(self):
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

        if (isCadeiaDeCaracteres != False and isExpressao != False) or (isCadeiaDeCaracteres == False and isExpressao == False):
            print("Operacao de escrever com entrada ambigua na linha " + lineno)
            exit()
    def getValue(self):
        return self.value
    def getIsExpressao(self):
        return self.isExpressao
    def getIsCadeiaDeCaracteres(self):
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
    
    def getScopeObj(self):
        return self.scope

    def setScopeObj(self,scope):
        self.scope = scope

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
        escopo["global"] = newScope
    else:
        escopo[id(newScope)] = newScope
    return newScope

####### Para percorrer a árvore#######

#PARA MONTAR O ESCOPO###
def walkTreeScopeStart(Tree,parent = None):
    localVariables = {}
    global escopo

    for x in Tree:
        localVariables[x] = Tree[x]
        if isinstance(Tree[x], Funcao):    
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

    Tree.setScopeObj(newParent)

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
    
    #é apenas uma expressão
    else: 
        pass
###FIM DAS FUNÇÕES DE MONTAR ESCOPO###

##PARA VERIFICAR TIPOS###

def walkTreeTypeStart(Tree):
    for x in Tree:
        if isinstance(Tree[x], Variable):
           pass

        elif isinstance(Tree[x], Funcao):
            walkTreeTypeFunction(Tree[x])
            

  
def walkTreeTypeFunction(Tree):
    x = Tree.getArvoreBloco()

    #print("Objeto Escopo :" + str(x.getScopeObj()))
    if x != None: 
        walkTreeTypeBloco(x,Tree.getTipo())
    

def walkTreeTypeBloco(Tree,tipoRetorno):
    x = Tree.getArvoreListComando()
    escopoAtual = Tree.getScopeObj()

    if x != None:
        walkTreeTypeListComando(x,tipoRetorno,escopoAtual)
    

def walkTreeTypeListComando(Tree,tipoRetorno,escopoAtual):
    
    if Tree != None:
        comando = Tree.getArvoreComando()
        listComando = Tree.getArvoreListComando()

        if comando != None:
            walkTreeTypeComando(comando,tipoRetorno,escopoAtual)
    
        if listComando != None:
            walkTreeTypeListComando(listComando,tipoRetorno,escopoAtual)
    
def walkTreeTypeComando(Tree,tipoRetorno,escopoAtual):

    if isinstance(Tree, Se):
        comandoSe = Tree.getComando()
        comandoSenao = Tree.getComandoSenao()
        expressao = Tree.getExpressao()

        if comandoSe != None:
            walkTreeTypeComando(comandoSe,tipoRetorno,escopoAtual)
        if comandoSenao != None:
            walkTreeTypeComando(comandoSenao, tipoRetorno,escopoAtual)

        if expressao != None:
            if walkTreeTypeExpressao(expressao,escopoAtual) != "int":
                print("Expressao da condicao nao inteira, erro na linha ", + str(expressao.getLineno()) )
                exit()

    elif isinstance(Tree, Enquanto):
        comando = Tree.getComando()
        expressao = Tree.getExpressao()

        if comando != None:
            walkTreeTypeComando(comando, tipoRetorno,escopoAtual)
        if expressao != None:
            if walkTreeTypeExpressao(expressao,escopoAtual) != "int":
                print("Expressao da condicao nao inteira, erro na linha ", + str(expressao.getLineno()) )
                exit()

    elif isinstance(Tree, Leia):
        lval = Tree.getArvoreLvalue()
        walkTreeTypeLval(lval,escopoAtual)
        pass

    elif isinstance(Tree, Escreva):
        #Expressao ou cadeia de caracteres
        value = Tree.getValue()
        if Tree.getIsExpressao() == True:
            if value != None:
                walkTreeTypeExpressao(value,escopoAtual)
            pass
        #Equivalente a Tree.getIsCadeiaDeCaracteres() == True
        else:
            #Não precisa verificar
            pass 

    elif isinstance(Tree, NovaLinha):
        pass

    elif isinstance(Tree, Retorne):
        expressao = Tree.getExpressao()
        if tipoRetorno != walkTreeTypeExpressao(expressao,escopoAtual):
            print("Tipo Retorno " + tipoRetorno)
            print("Tipo retornado diferente do enunciado, erro na linha "+ str(Tree.getLineno()) )
            exit()
        pass

    elif isinstance(Tree, Bloco):
        walkTreeTypeBloco(Tree,tipoRetorno)

    #é apenas uma expressão
    else:
        walkTreeTypeExpressao(Tree,escopoAtual)
        pass

def walkTreeTypeExpressao(Tree,escopoAtual):
    #Essa variavel PRECISA retornar algo diferente de vazio
    tipoExpressao = None

    if isinstance(Tree, Atribuicao):
        lval = Tree.getArvoreLval()
        atribuicao = Tree.getArvoreAtribuicao()
        tipo1 = walkTreeTypeLval(lval, escopoAtual)
        tipo2 = walkTreeTypeExpressao(atribuicao,escopoAtual) 

        if tipo1 != tipo2:
            print("Atribuicao de tipos diferentes, erro linha "+ str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = tipo1 

    elif isinstance(Tree, Condicional):
        ou  = Tree.getArvoreOu()
        expressao = Tree.getArvoreExpressao()
        condicional = Tree.getArvoreCondicional()
        tipoOu = walkTreeTypeExpressao(ou,escopoAtual)

        if tipoOu != "int":
            print("expressao condicional nao inteira, erro linha "+ str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = "int"
        
    elif isinstance(Tree, Ou):
        ou = Tree.getArvoreOu()
        e = Tree.getArvoreE()
        tipo1 = walkTreeTypeExpressao(ou,escopoAtual)
        tipo2 = walkTreeTypeExpressao(e,escopoAtual)

        if tipo1 != tipo2:
            print("Comparacao entre tipos diferentes, erro linha "+ str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = tipo1

    elif isinstance(Tree, E):
        e = Tree.getArvoreE()
        equivalente = Tree.getArvoreEquivalente()
        tipo1 = walkTreeTypeExpressao(e,escopoAtual)
        tipo2 = walkTreeTypeExpressao(equivalente,escopoAtual)

        if tipo1 != tipo2:
            print("Comparacao entre tipos diferentes, erro linha " + str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = tipo1
    
    elif isinstance(Tree, Equivalente):
        equivalente = Tree.getArvoreEquivalente()
        desigualdade = Tree.getArvoreDesigualdade()
        tipo1 = walkTreeTypeExpressao(equivalente,escopoAtual)
        tipo2 = walkTreeTypeExpressao(desigualdade,escopoAtual)

        if tipo1 != tipo2:
            print("Comparacao entre tipos diferentes, erro linha " + str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = tipo1
        
    
    elif isinstance(Tree, Desigualdade):
        desigualdade = Tree.getArvoreDesigualdade()
        adicao = Tree.getArvoreAdicao()
        tipo1 = walkTreeTypeExpressao(desigualdade,escopoAtual) 
        tipo2 = walkTreeTypeExpressao(adicao,escopoAtual)

        if tipo1 != tipo2:
            print("Comparacao entre tipos diferentes, erro linha " + str(Tree.getLineno()) )
            exit()
        else:
            tipoExpressao = tipo1
        
    
    elif isinstance(Tree, Adicao):
        adicao = Tree.getArvoreAdicao()
        multiplicacao = Tree.getArvoreMultiplicacao()
        tipo1 = walkTreeTypeExpressao(adicao,escopoAtual)
        tipo2 = walkTreeTypeExpressao(multiplicacao,escopoAtual)

        if tipo1 == "int" and tipo2 == "int":
            tipoExpressao = tipo1
        else:
            print("Adicao com tipo nao inteiro , erro linha " + str(Tree.getLineno()))
            exit()
        
    elif isinstance(Tree, Multiplicacao):
        multiplicacao = Tree.getArvoreMultiplicacao()
        unary = Tree.getArvoreUnitaria()
        tipo1 = walkTreeTypeExpressao(multiplicacao,escopoAtual)
        tipo2 = walkTreeTypeExpressao(unary,escopoAtual)
        
        if tipo1 == "int" and tipo2 == "int":
            tipoExpressao = tipo1
        else:
            print("Produto com tipo nao inteiro , erro linha " + str(Tree.getLineno()) )
            exit()

    elif isinstance(Tree, UnaryExpr):
        prim = Tree.getArvorePrimExpr()
        tipo = walkTreeTypePrimExpr(prim,escopoAtual)
        
        if tipo != "int":
            print("Operacao so aceita inteiro, erro linha " + str(Tree.getLineno()))
            exit()
        else:
            tipoExpressao = tipo
        
    elif isinstance(Tree, PrimExpr):
        tipoExpressao = walkTreeTypePrimExpr(Tree,escopoAtual)


    #print("Retornando " + str(tipoExpressao))
    return tipoExpressao


def walkTreeTypeLval(Tree, escopoAtual):
    expressao = Tree.getExpressao()
    
    if expressao != None:
        tipoExp = walkTreeTypeExpressao(expressao,escopoAtual)
        if tipoExp != "int":
            print("Expressao nao inteira, erro linha "+ str(Tree.getLineno()) )
            exit()

    identificador = Tree.getId()

    tipo = getVarType(identificador,escopoAtual)
    
    if tipo == None:
        print("Variavel "+identificador+"nao declarada, erro na linha "+ str(Tree.getLineno()) )
        exit()

    return tipo

def walkTreeTypePrimExpr(Tree,escopoAtual):
    
    #Se for só uma expressao
    if Tree.getIsExpression() == True:
        return walkTreeTypeExpressao(Tree.getArvoreListExpr(),escopoAtual)

    #Se for uma variavel
    if Tree.getIsVariable() == True:
        tipo = getVarType(Tree.getIdentificador(),escopoAtual)

        if tipo == None:
            print("Variavel "+Tree.getIdentificador()+"nao declarada, erro na linha "+ str(Tree.getLineno()) )
            exit()
        
        expressao = Tree.getArvoreListExpr()
        if expressao != None:
            walkTreeTypeExpressao(expressao,escopoAtual)
        
        return tipo

    #Se for uma constante
    if Tree.getIsCar() == True:
        return "car"
    if Tree.getIsInt() == True:
        return "int"
    
    if Tree.getIsFunction() == True:
        tipo = getVarType(Tree.getIdentificador(),escopoAtual)
        if tipo == None:
            print("Funcao "+Tree.getIdentificador()+" nao declarada, erro na linha "+ str(Tree.getLineno()) )
            exit()
        #navegar no listExpressao
        lexpr = Tree.getArvoreListExpr()
        if lexpr == None:
            print("Funcao "+Tree.getIdentificador()+"nao declarando corretamente, erro na linha "+ str(Tree.getLineno()))
            exit()

        print("FUI CHAMADO!!!!")
        walkTreeTypeListExpr(lexpr,escopoAtual)

        return tipo

def walkTreeTypeListExpr(Tree,escopoAtual):
   
    if isinstance(Tree,ListExpr) == True:
        assignexpr = Tree.getArvoreAtribuicao()
        listexpr = Tree.getArvoreListExpr()
        print("ENTREI "+ str(Tree.getLineno()))

        walkTreeTypeExpressao(assignexpr,escopoAtual)

        if listexpr != None:
            walkTreeTypeListExpr(listexpr,escopoAtual)

    elif isinstance(Tree, Atribuicao) == True:
        walkTreeTypeExpressao(Tree,escopoAtual)


def getVarType(identificador,escopoAtual):
    global escopo
    dicionarioAtual = {}

    #print("Procurando "+identificador+" no escopo "+ str(escopoAtual))

    #se for uma string significa que o escopo é o "global"
    if isinstance(escopoAtual, str):
        dicionarioAtual = escopo["global"].getVariableDict()
        #print(dicionarioAtual)
        if identificador in dicionarioAtual:
            return dicionarioAtual[identificador].getTipo()
        else:
            return None
    
    dicionarioAtual = escopo[id(escopoAtual)].getVariableDict()

    if identificador in dicionarioAtual:
        return dicionarioAtual[identificador].getTipo()
    else:
        return getVarType(identificador,escopo[id(escopoAtual)].getParent()) 

    
###FIM DA VERIFICAÇÃO DE TIPOS


##FIM DE ANDAR NA ÁRVORE###
