import ply.lex as lex

tokens = (
    'token_llave_izq',
    'token_llave_der',
    'token_cor_izq',
    'token_cor_der',
    'token_par_izq',
    'token_par_der',
    'token_mayor',
    'token_menor',
    'token_mayor_igual',
    'token_menor_igual',
    'token_igual_num',
    'token_point',
    'token_diff_num',
    'token_and',
    'token_or',
    'token_not',
    'token_mas',
    'token_menos',
    'token_mul',
    'token_div',
    'token_mod',
    'token_pot',
    'token_assign',
    'token_coma',
    'token_dosp',
    'while',
    'for',
    'if',
    'else',
    'log',
    'funcion',
    'identificador',
    'string',
    'false',
    'true',
    'in',
    'end',
    'retorno',
    'token_float',
    'token_integer',
)

states = (
    ('comment','exclusive'),
)

t_token_llave_izq = r'{'
t_token_llave_der = r'}'
t_token_cor_izq = r'\['
t_token_cor_der = r'\]'
t_token_par_izq = r'\('
t_token_par_der = r'\)'
t_token_mayor = r'>'
t_token_menor = r'<'
t_token_mayor_igual = r'>='
t_token_menor_igual = r'<='
t_token_igual_num = r'=='
t_token_point = r'\.'
t_token_diff_num = r'!='
t_token_and = r'&&'
t_token_or = r'\|\|'
t_token_not = r'!'
t_token_mas = r'\+'
t_token_menos = r'-'
t_token_mul = r'\*'
t_token_div = r'/'
t_token_mod = r'%'
t_token_pot = r'\^'
t_token_assign = r'='
t_token_coma = r','
t_token_dosp = r':'

def t_while(token):
    r'while'
    token.type = 'while'
    return token

def t_for(token):
    r'for'
    token.type = 'for'
    return token

def t_if(token):
    r'if'
    token.type = 'if'
    return token

def t_else(token):
    r'else'
    token.type = 'else'
    return token

def t_funcion(token):
    r'funcion'
    token.type = 'funcion'
    return token

def t_false(token):
    r'false'
    token.type = 'false'
    return token

def t_true(token):
    r'true'
    token.type = 'true'
    return token

def t_in(token):
    r'in'
    token.type = 'in'
    return token

def t_end(token):
    r'end'
    token.type = 'end'
    return token

def t_retorno(token):
    r'retorno'
    token.type = 'retorno'
    return token

def t_log(token):
    r'log'
    token.type = 'log'
    return token

def t_identificador(token):
    r'[a-zA-Z][a-zA-Z_]*'
    token.value = token.value
    return token

def t_token_float(token):
    r'-?[0-9]+\.[0-9]+'
    token.value = float(token.value)
    return token

def t_token_integer(token):
    r'-?[0-9]+'
    token.value = int(token.value)
    return token

def t_string(token):
    r'"(?:[^"\\]|(?:\\.))*"'
    token.value = token.value[1:-1]
    return token

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

t_ignore  = ' \t\v\r'

def t_begin_comment(token):
    r'\#'
    token.lexer.begin('comment')

def t_comment_end(token):
    r'\n'
    token.lexer.lineno += len(token.value)
    token.lexer.begin('INITIAL')

def t_comment_error(token):
    token.lexer.skip(1)

def t_error(t):
    print("Error léxico (linea : " + str(t.lexer.lineno) +", posición : "+ str(t.lexer.lexpos)+ ")")
    t.lexer.skip(1)

lexer = lex.lex()

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def test_lexer(input_string):
    lexer.input(input_string)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if(tok.value == tok.type):
            print("<" + tok.type +"," + str(tok.lineno) + "," + str(find_column(input_string,tok)) + ">")
        else:
            print("<"+tok.type+","+str(tok.value)+","+str(tok.lineno)+","+str(find_column(input_string,tok))+">")

file = open("test.txt","r")
input = file.read()
file.close()

print(input)
print(test_lexer(input))