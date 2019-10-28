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
            print("Erro na linha "+str(p.lineno) +
                  ":variavel "+ "já foi declarada")
            exit()
        else:
            variableList[str(p[2])] = x
        p[0] = variableList


def p_declprog(p):
    'declprog : PROGRAMA bloco'
    #print("declprog")
    #p[0] = p[0] + p[1]

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

        print(p[2])
        if  p[2] in variableList:
            print("Erro na linha "+str(p.lineno)+ ":variavel " + "já foi declarada")
            exit()
        else:
            variableList[str(p[2])] = x
        
        p[0] = variableList

            
    #print("declvar")
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 7:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
    #if len(p) == 1:
    #    p[0] = []

def p_declfunc(p):
    'declfunc : ABREPARENTESES listaparametros FECHAPARENTESES bloco'

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
      #      print(p[3])
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
            print("Erro na linha "+str(p.lineno)+":variavel " + "já foi declarada")
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

    #print("expr")
    #if len(p) == 2:
    #    p[0] = p[1]

def p_assignexpr(p):
    """
    assignexpr : condexpr
    assignexpr : lvalueexpr IGUAL assignexpr
    """

    #print("assignexpr")
    #if len(p) == 2:
    #    p[0] = p[1]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]

def p_condexpr(p):
    """
    condexpr : orexpr
    condexpr : orexpr INTERROGACAO expr DOISPONTOS condexpr
    """

    #print("condexpr")
    #if len(p) == 2:
    #    p[0] = p[1]
    #if len(p) == 6:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_orexpr(p):
    """
    orexpr : orexpr OU andexpr
    orexpr : andexpr
    """

    #print("orexpr")
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_andexpr(p):
    """
    andexpr : andexpr E eqexpr
    andexpr : eqexpr
    """

    #print("andexpr")
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_eqexpr(p):
    """
    eqexpr : eqexpr IGUALIGUAL desigexpr
    eqexpr : eqexpr EXCLAMACAO IGUAL desigexpr
    eqexpr : desigexpr
    """

    #print("eqexpr")
    #expressoes com mesmo tamanho
    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_desigexpr(p):
    """
    desigexpr : desigexpr MENOR addexpr
    desigexpr : desigexpr MAIOR addexpr
    desigexpr : desigexpr MAIOR IGUAL addexpr
    desigexpr : desigexpr MENOR IGUAL addexpr
    desigexpr : addexpr
    """
    
    #print("desigexpr")
    #expressoes com mesmo tamanho

    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_addexpr(p):
    """
    addexpr : addexpr MAIS mulexpr
    addexpr : addexpr MENOS mulexpr
    addexpr : mulexpr
    """

    #print("addexpr")
    #expressoes com mesmo tamanho

    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_mulexpr(p):
    """
    mulexpr : mulexpr VEZES unexpr
    mulexpr : mulexpr DIVIDE unexpr
    mulexpr : mulexpr PERCENTUAL unexpr
    mulexpr : unexpr
    """

    #print("mulexpr")
    #expressoes com mesmo tamanho

    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 2:
    #    p[0] = p[1]

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

    #print("lvalueexpr")
    
    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_primexpr(p):
    """
    primexpr : ID ABREPARENTESES listexpr FECHAPARENTESES 
    primexpr : ID ABREPARENTESES FECHAPARENTESES
    primexpr : ID ABRECOLCHETES expr FECHACOLCHETES
    primexpr : ID
    primexpr : CARCONST
    primexpr : INTCONST
    primexpr : ABREPARENTESES expr FECHAPARENTESES
    """

    #expressoes com mesmo tamanho

    #if len(p) == 5:
    #    p[0] = p[1] + p[2] + p[3] + p[4]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]
    #if len(p) == 2:
    #    p[0] = p[1]

def p_listexpr(p):
    """
    listexpr : assignexpr
    listexpr : listexpr VIRGULA assignexpr
    """

    #print("listexpr")
    #if len(p) == 2:
    #    p[0] = p[1]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3]

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
