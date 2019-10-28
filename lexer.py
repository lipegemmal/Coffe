# -*- coding: utf-8 -*-

from ply import lex 

#palavras reservadas
reserved = {
    'programa' : 'PROGRAMA',
    'car' : 'CAR',   #tipo caracter 
    'int' : 'INT',   #tipo inteiro
    'retorne' : 'RETORNE',
    'leia' : 'LEIA',
    'escreva' : 'ESCREVA',
    'novalinha' : 'NOVALINHA',
    'se' : 'SE' ,
    'entao' : 'ENTAO',
    'senao' : 'SENAO',
    'enquanto' : 'ENQUANTO', 
    'execute' : 'EXECUTE',
    #'cadeiaCaracteres'

    #operadores logicos e e ou
    'e' : 'E',
    'ou' : 'OU'

}

###Lista de tokens###
tokens = [
    #Simbolos matemáticos, aqui escritos por extenso para nomear o token
    'MAIS',     # +
    'MENOS',    # -
    'VEZES',    # *
    'DIVIDE',   # /
    'PERCENTUAL',  # %
    
    #Simbolos lógicos
    'MENOR',   # <
    'MAIOR',   # >
    'IGUALIGUAL', #==
    'IGUAL',   # =
   # 'E',       # e
   # 'OU',      # ou
    'EXCLAMACAO',  # !
    'INTERROGACAO', # ?

    #Simbolos de operação
    'ABREPARENTESES',   # (
    'FECHAPARENTESES',  # )
    'ABRECOLCHETES',    # [
    'FECHACOLCHETES',   # ]
    'ABRECHAVES',       # {
    'FECHACHAVES',      # }
    'DOISPONTOS',       # :
    'VIRGULA',          # ,
#    'ASPASDUPLAS',      # "
    'PONTOEVIRGULA',    # ;

    
    'CARCONST',
    'INTCONST',
    'CADEIACARACTERES',

    #Variavel + palavras reservadas da lista (faço a checagem)
    'ID',

    #Simbolo de linha
    'BARRAN',    # \n

    #Comentário
    'COMENTARIOMULTILINHA',
    'COMENTARIOUMALINHA'
] + list(reserved.values())

###Expressões regulares###


def t_COMENTARIOMULTILIHA(t):
    r'/\*[^(\*/)]*(\*/)?'

    
    if t.value[len(t.value)-2] != '*' and t.value[len(t.value)-1] != '/':
        print("ERRO: COMENTÁRIO NAO TERMINA, erro linha:"+ str(t.lexer.lineno))
        exit() 
    
    t.lexer.lineno += t.value.count('\n')

    pass

def t_COMENTARIOUMALINHA(t):
    r'// .*  '
    t.lexer.lineno += 1
    pass

#Simbolos matematicos
t_MAIS = '\+'
t_MENOS = '\-'
t_VEZES = '\*'
t_DIVIDE = '\/'
t_PERCENTUAL = '\%'

#Simbolos lógicos
t_MENOR = '\<'
t_MAIOR = '\>'
t_IGUALIGUAL = '\=\='
t_IGUAL = '\='
t_EXCLAMACAO = '\!'
t_INTERROGACAO = '\?'

#Simbolos de operacao
t_ABREPARENTESES = '\('
t_FECHAPARENTESES = '\)'
t_ABRECOLCHETES = '\['
t_FECHACOLCHETES = '\]'
t_ABRECHAVES = '\{'
t_FECHACHAVES = '\}'
t_DOISPONTOS = '\:'
t_VIRGULA = '\,'
t_PONTOEVIRGULA = '\;'

#incrementa a linha do programa 
def t_BARRAN(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#car não pode ser "
def t_CARCONST(t):
    r' \'[^\']\' '
    t.value = t.value[1:-1]
    return t

def t_INTCONST(t):
    r'[0-9][0-9]*'
    t.value = int(t.value)
    return t

#cadeia não aceita " dentro 
def t_CADEIACARACTERES(t):
    r' \"[^"]+\" '
    t.value = t.value[1:-1]
    if t.value.find('\n') != -1:
       print("ERRO: CADEIA DE CARACTERES OCUPA MAIS DE UMA LINHA, erro linha:" + str(t.lexer.lineno))
       print(t)
       exit()
    return t


#Variavel
def t_ID(t): 
    r'[a-zA-Z][a-zA-Z0-9]*' #ID's começam com uma letra e depois só aceitam letras e números (sem caracteres especiais)
    t.type = reserved.get(t.value,'ID')
    return t


def t_error(t):
    print("ERRO: CARACTERE INVÁLIDO, na linha:" + str(t.lexer.lineno))
    exit()

t_ignore = ' \t\r'



lexer = lex.lex()


if __name__ == "__main__":
    print("Digite o nome do arquivo de entrada (com o tipo dele):")
    pasta = "arquivos/"
    entrada = input()

    #print(pasta+entrada)
    
    arquivo = open(pasta + str(entrada) ,"r").read()
    lex.input(arquivo)
    
    while True:
        tok = lexer.token()   
        if not tok:
            break
        print(" Token:\"" + str(tok.value) + "\" Lineno:"+ str(tok.lineno))



