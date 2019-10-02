from ply import yacc

#importing lexer object
from lexer import lexer
#import tokens table
from lexer import tokens



##
##  REANALIZAR A CADEIA DE CARACTERES!!!
##  VERIFICAR NUMBER, CONSTINT, CARCONST E ASPASDUPLAS , CADEIADECARACTERES

def p_programa(p):
    "programa : declfuncvar declprog"

    #print("Sai")
    #p[0] = p[1] + p[2]

def p_declfuncvar(p):
    """
    declfuncvar : tipo ID declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo ID ABRECOLCHETES INTCONST FECHACOLCHETES declvar PONTOEVIRGULA declfuncvar
    declfuncvar : tipo ID declfunc declfuncvar
    declfuncvar : 
    """

    #print("declfuncvar")
    #if len(p) == 6:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] 
    #if len(p) == 9:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[9]
    #if len(p) == 4:
    #    p[0] = p[1] + p[2] + p[3] 
    #if len(p) == 1:
    #    p[0] = []

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
    listadeclvar : 
    listadeclvar : tipo ID declvar PONTOEVIRGULA listadeclvar
    listadeclvar : tipo ID ABRECOLCHETES INTCONST FECHACOLCHETES declvar PONTOEVIRGULA listadeclvar
    """

    #print("listadeclvar")
    #if len(p) == 1:
    #    p[0] = []
    #if len(p) == 6:
    #    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_tipo(p):
    """
    tipo : INT
    tipo : CAR
    """
    
    #print("tipo")
    #duas regras com mesmo tamanho
    #if len(p) == 2:
    #    p[0] = p[1]

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

    #print("primexpr")
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
    print("ERRO, token " + p.type + " na linha " + str(p.lineno))
    #print (p.__dict__.keys())
    exit

parser = yacc.yacc()

#yacc.parse(open("test.txt","r"))

s = open("test.txt","r").read()

#parser.parse(s, tracking=True)
parser.parse(s)