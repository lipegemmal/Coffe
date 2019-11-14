from ply import yacc
#importing lexer object
from lexer import lexer
#import tokens table
from lexer import tokens
#Classes file
import classes as objects

##
##  REANALIZAR A CADEIA DE CARACTERES!!!
##  VERIFICAR NUMBER, CONSTINT, CARCONST E ASPASDUPLAS , CADEIADECARACTERES

def p_programa(p):
    "programa : declfuncvar declprog"

    print(p[1])
    #if isinstance(lista['x'],objects.Variable):
     

def p_declfuncvar(p):
    """
    declfuncvar : tipo ID declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo ID ABRECOLCHETES INTCONST FECHACOLCHETES declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo ID declfunc declfuncvar
    declfuncvar : 
    """

    
    #PARA AS DECLARAÇÕES DE VARIAVEL GLOBAL
    if len(p) > 5:
        variableList = {}
        Repetido = False
        x = None
        #Se é um vetor
        if p[3] == "[":
            x = objects.Variable(vector=True, vectorSize=p[4])
            #pegando recursão
            if p[8] != None:
                variableList = p[8]
            #pegando valor de declvar
            if p[6] != None:
                auxList = p[6]
                for aux in auxList:
                    auxList[aux].setTipo(str(p[1]))
                    if aux in variableList:
                        Repetido = True
                        break
                variableList.update(auxList)

        #Se é uma variavel
        else:
            x = objects.Variable()
            #pegando recursão
            if p[5] != None:
                variableList = p[5]
            #pegando valor de declvar
            if p[3] != None:
                auxList = p[3]
                for aux in auxList:
                    auxList[aux].setTipo(str(p[1]))
                    if aux in variableList:
                        Repetido = True
                        break
                variableList.update(auxList)

        #print(p[2])
        if p[2] in variableList or Repetido == True:
            print("Erro na linha "+str(p.lineno(2)) +
                  ":variavel "+ "já foi declarada")
            exit()
        else:
            variableList[str(p[2])] = x
        p[0] = variableList
        aux = objects.createScope(variableList,None)

        #print(objects.escopo)


def p_declprog(p):
    'declprog : PROGRAMA bloco'
    #Aqui é o escopo "main"



def p_declvar(p):
    """
    declvar : VIRGULA ID declvar
    declvar : VIRGULA ID ABRECOLCHETES INTCONST FECHACOLCHETES declvar
    declvar :
    """

    #print("declvar")
    variableList = {}
    if len(p) > 1:
        x = None
        #Se é um vetor
        if p[3] == "[":
            x = objects.Variable(vector=True, vectorSize=p[4])
            if p[6] != None:
                variableList = p[6]
        #Se é uma variavel
        else:
            x = objects.Variable()
            if p[3] != None:
                variableList = p[3]

       # print(p[2])
        if  p[2] in variableList:
            print("Erro na linha "+str(p.lineno(2))+ ":variavel " + "já foi declarada")
            exit()
        else:
            variableList[str(p[2])] = x
        
        p[0] = variableList

def p_declfunc(p):
    'declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco'

   # print("blocoDeclFunc")
    #print("declfunc")
    #p[0] = p[1] + p[2] + p[3] + p[4]

def p_listaparametros(p):
    """
    listaparametros : 
    listaparametros : listaparametroscont
    """

    #print("listaparametros")
    #if len(p) == 1:
    #    p[0] = []
    #if len(p) == 2:
    #    p[0] = p[1]

def p_listaparametroscont(p):
    """
    listaparametroscont : tipo ID
    listaparametroscont : tipo ID ABRECOLCHETES FECHACOLCHETES
    listaparametroscont : tipo ID VIRGULA listaparametroscont
    listaparametroscont : tipo ID ABRECOLCHETES FECHACOLCHETES VIRGULA listaparametroscont
    """

    #print("listaparametroscont")
    #if len(p) == 3:
    #    p[0] = p[1] + p[2]
    #note que existem duas regras com o mesmo len
    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 7:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_bloco(p):
    """
    bloco : ABRECHAVES listadeclvar listacomando FECHACHAVES
    bloco : ABRECHAVES listadeclvar FECHACHAVES
    """
    
    #SUBIR P[2] ṔARA DETERMINAR O PAI
    


    #print("bloco")
    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]

def p_listadeclvar(p):
    """
    listadeclvar : tipo ID declvar PONTOEVIRGULA listadeclvar
    listadeclvar : tipo ID ABRECOLCHETES INTCONST FECHACOLCHETES declvar PONTOEVIRGULA listadeclvar
    listadeclvar : 
    """

    #print("listadeclvar de tamanho " + str(len(p)))
    variableList = {}
    Repetido = False
    #Se não é vazio
    if len(p) > 1:
        #Se é uma variavel comum
        if p[4] == ';':
            x = objects.Variable(p[1])
            #pegando recursão
            if p[5] != None:
                variableList = p[5]
            #pegando declvar
            if p[3] != None:
                auxList = p[3]
                for aux in auxList:
                    auxList[aux].setTipo(str(p[1]))
                    if aux in variableList:
                        Repetido = True
                        break
                variableList.update(auxList)
      #print(p[3])
        #Se é um vetor
        else:
            x = objects.Variable(p[1],True,p[4])
            #pegando recursão
            if p[8] != None:
                variableList = p[8]
            #pegando declvar
            if p[6] != None:
                auxList = p[6]
                for aux in auxList:
                    auxList[aux].setTipo(str(p[1]))
                    if aux in variableList:
                        Repetido = True
                        break
                variableList.update(auxList)

        if p[2] in variableList or Repetido == True:
            print("Erro na linha "+str((p.lineno(2)))+":variavel " + "já foi declarada")
            exit()
        else:
            variableList[str(p[2])] = x
            
       
    p[0] = variableList

def p_tipo(p):
    """
    tipo : INT
    tipo : CAR
    """
    #subindo tipo para declarar uma variavel
    p[0] = p[1]


def p_listacomando(p):
    """
    listacomando : comando
    listacomando : comando listacomando
    """

    #print("listacomando")
    #if len(p) == 2:
    #    p[0] = p[1]
    #if len(p) == 3:
    #    p[0] = p[1] + p[2]

def p_comando(p):
    """
    comando : PONTOEVIRGULA
    comando : expr PONTOEVIRGULA
    comando : RETORNE expr PONTOEVIRGULA
    comando : LEIA lvalueexpr PONTOEVIRGULA    
    comando : ESCREVA expr PONTOEVIRGULA
    comando : ESCREVA CADEIACARACTERES PONTOEVIRGULA
    comando : NOVALINHA PONTOEVIRGULA
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando
    comando : SE ABREPARENTESES expr FECHAPARENTESES ENTAO comando SENAO comando
    comando : ENQUANTO ABREPARENTESES expr FECHAPARENTESES EXECUTE comando
    comando : bloco
    """ 


    #p[0] = objects.Enquanto(expr,comando)

    #print("blocoComando")
    #print("comando")
    #varios comandos com mesmos tamanhos
    #if len(p) == 2:
    #    p[0] = p[1]
    #if len(p) == 3:
    #    p[0] = p[1] + p[2]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 6:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    #if len(p) == 7:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]


def p_expr(p):
    'expr : assignexpr'

    #Não crio objeto expressão pois ele já vem montado da atribuicao
    #Só precisa então subir o objeto
    p[0] = p[1]

def p_assignexpr(p):
    """
    assignexpr : condexpr
    assignexpr : lvalueexpr IGUAL assignexpr
    """

    x = None
    #Se é uma atribuicao com =
    if len(p) == 4:
        x = objects.Atribuicao(p[1],p[3])
    #Só subo o objeto condicional
    else:
        x = p[1]
    p[0] = x

def p_condexpr(p):
    """
    condexpr : orexpr
    condexpr : orexpr INTERROGACAO expr DOISPONTOS condexpr
    """

    x = None   
    #Se é uma expressao condicional
    if len(p) == 6:
        x = objects.Condicional(p[1],p[3],p[5])
    #Só subo o objeto Ou
    else:
        x = p[1]
    p[0] = x
    
def p_orexpr(p):
    """
    orexpr : orexpr OU andexpr
    orexpr : andexpr
    """

    x = None
    #para uma expressao com OU
    if len(p) == 4:
        x = objects.Ou(p[1],p[3])
    #Só subo a arvore E
    else:
        x = p[1]    
    p[0] = x

def p_andexpr(p):
    """
    andexpr : andexpr E eqexpr
    andexpr : eqexpr
    """
    
    x = None
    #para uma expressao com E
    if len(p) == 4:
        x = objects.E(p[1], p[3])
    #Só subo a arvore Equivalencia
    else:
        x = p[1]
    p[0] = x

def p_eqexpr(p):
    """
    eqexpr : eqexpr IGUALIGUAL desigexpr
    eqexpr : eqexpr EXCLAMACAO IGUAL desigexpr
    eqexpr : desigexpr
    """

    x = None
    #Expressao de igualdade ==
    if len(p) == 4:
        x = objects.Equivalente(p[1],p[3],True)
    #Expressao de diferente !=
    elif len(p) == 4:
        x = objects.Equivalente(p[1],p[4],False)
    #Só subo a arvore de deseigualdade
    else:
        x = p[1]

    p[0] = x

def p_desigexpr(p):
    """
    desigexpr : desigexpr MENOR addexpr
    desigexpr : desigexpr MAIOR addexpr
    desigexpr : desigexpr MAIOR IGUAL addexpr
    desigexpr : desigexpr MENOR IGUAL addexpr
    desigexpr : addexpr
    """
    
    x = None
    #Desigualdade sem = 
    if len(p) == 4:
        #Se a operação é um >
        if p[2] == ">":
            x = objects.Desigualdade(p[1],p[3],Maior=True,Igual=False)
        else:
            x = objects.Desigualdade(p[1],p[3],Maior=False,Igual=False)
    #Desigualdade com =
    elif len(p) == 5:
        #Se a operação é um >
        if p[2] == ">":
            x = objects.Desigualdade(p[1],p[4],Maior=True,Igual=True)
        else:
            x = objects.Desigualdade(p[1],p[4],Maior=False,Igual=True)
    #Só subo a árvore de adição
    else:
        x = p[1]
    
    p[0] = x
    
def p_addexpr(p):
    """
    addexpr : addexpr MAIS mulexpr
    addexpr : addexpr MENOS mulexpr
    addexpr : mulexpr
    """

    x = None
    if len(p) == 4:
        #Se a operação é de +
        if p[2] == "+":
           x = objects.Adicao(p[1],p[3],Mais = True) 
        #Se a operação é de -
        else:
            x = objects.Adicao(p[1],p[3],Mais = False)
    #Só subo a árvore de multiplicação
    else:
        x = p[1]
    
def p_mulexpr(p):
    """
    mulexpr : mulexpr VEZES unexpr
    mulexpr : mulexpr DIVIDE unexpr
    mulexpr : mulexpr PERCENTUAL unexpr
    mulexpr : unexpr
    """

    x = None
    #Se a árvore deve ser montada
    if len(p) == 4:
        #Se a operação é de Vezes
        if p[2] == "*":
            x = objects.Multiplicacao(p[1],p[3],Vezes=True)
        #Se a operação é de Divisao
        elif p[2] == "/":
            x = objects.Multiplicacao(p[1],p[3],Divisao=True)
        #Se a operação é de resto da divisao (%)
        elif p[2] == "%":
            x = objects.Multiplicacao(p[1], p[3],Resto=True)

    #Só subo a árvore unitária
    else:
        x = p[1]
        
    p[0] = x

def p_unexpr(p):
    """
    unexpr : MENOS primexpr
    unexpr : EXCLAMACAO primexpr
    unexpr : primexpr
    """
    #print("unexpr")
    #expressoes com mesmo tamanho

    #if len(p) == 3:
    #    p[0] = p[1] + p[2]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_lvalueexpr(p):
    """
    lvalueexpr : ID ABRECOLCHETES expr FECHACOLCHETES
    lvalueexpr : ID
    """
    
    x = None
    #Se o identificador acessado é um vetor
    if len(p) == 5:
        x = objects.Lval(p[1],p[3])
    #Se o identificador acessado não é um vetor, exp = None no objeto
    else:
        x = objects.Lval(p[1])

    p[0] = x
def p_primexpr1(p):
    """
    primexpr : ID ABREPARENTESES listexpr FECHAPARENTESES 
    primexpr : ID ABREPARENTESES FECHAPARENTESES
    primexpr : ID ABRECOLCHETES expr FECHACOLCHETES
    primexpr : ID
    primexpr : ABREPARENTESES expr FECHAPARENTESES
    """
    #expressoes com mesmo tamanho

    x = None

    #Pode ser chamada de função ou uma posição de vetor
    if len(p) == 5:
        #Se for uma chamada de função
        if p[2] == "(":
            x = objects.Primexpr(p[1],p[3],isFunction=True)
        #Se for uma posição de vetor (acesso a vetor)
        else:
            x = objects.Primexpr(p[1],arvoreAtribuicao=p[3],isVariable=True)
    elif len(p) == 4:
        #Se for uma chamada de função sem parâmetros
        if p[2] == "(":
            x = objects.Primexpr(p[1],isFunction=True)
        #Se for uma expressao entre parenteses
        else:
            x = objects.Primexpr(arvoreListExpr=p[2],isExpression=True)
    #Apenas um ID (Variavel ou endereço de vetor)
    else:
        x = objects.Primexpr(p[1],isVariable=True)

    p[0] = x

def p_primexpr2(p):
    """
    primexpr : CARCONST
    """

    x = objects.Primexpr(valorConstante=p[1],isCar=True)
    p[0] = x


def p_primexpr3(p):
    """
    primexpr : INTCONST
    """
    x = objects.Primexpr(valorConstante=p[1],isInt=True)
    p[0] = x

def p_listexpr(p):
    """
    listexpr : assignexpr
    listexpr : listexpr VIRGULA assignexpr
    """
    #Posso tanto criar uma lista quanto uma árvore, usarei árvore para manter o padrão    
    x = None

    #Se a instancia atual é uma cadeia de expressoes separadas por virgula
    if len(p) == 4:
        x = objects.ListExpr(p[1],p[3])
    #Se a instancia atual é apenas uma expressao
    else:
        x = p[1]
    p[0] = x
        

    

def p_error(p):
    print("ERRO, token " + p.type + " nao esperado na linha " + str(p.lineno))
    #print (p.__dict__.keys())
    exit()


print("Digite o nome do arquivo de entrada (com o tipo dele):")

pasta = "arquivos/"
entrada = input()   
arquivo = open(pasta + str(entrada) ,"r").read()

parser = yacc.yacc()

#yacc.parse(open("test.txt","r"))

#parser.parse(s, tracking=True)
parser.parse(arquivo)

print("Nenhum erro encontrado")
