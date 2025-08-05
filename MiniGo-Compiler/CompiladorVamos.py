#Integrantes
#Christian Geovanni De La Cruz Rodríguez

ERR = -1
ACP = 999
idx = 0
errB = False
entrada = ''
tok = ''
lex = ''
archE = ''
nomIde = ''
nombre_func = ''
finB = ''
bImp = False
bCiclo = False
bDim = False
bRetorno = False
bRegresa = False
reng = 1
colu= 1
conLin = 1
conEtiq = 1
pTipos = []
pRetorno = []
clase = 'I'
Operacion = ''
variable =''
cteLog=['verdadero', 'falso']
palRes=['interrumpe', 'otro', 'func', 'interface', 'selecciona',
'caso', 'difiere', 'ir', 'mapa', 'estructura','fmt', 'Leer', 'Imprime'
'canal', 'sino', 'ir_a', 'paquete', 'segun', 'principal','Imprimenl',
'const', 'si' , 'rango', 'tipo', 'entero', 'decimal', 'logico', 'Lmp',
'alfabetica','continua', 'desde', 'importar', 'regresa', 'var']

progm = {}

def insCodigo(codPL0):
    global progm, conLin
    progm[conLin] = codPL0
    conLin = conLin + 1

def impCod(linC, cod):
    print(linC, cod[0]+' '+cod[1]+', ' + cod[2])

matran=[
    #                                          , : 
    #                   %                       ()             
    #                   -           >           {}             
    #_|let  digito  .   +   /   \n  <   =   "   []  |   &   !   *
    [1,     2,      14, 5,  6,  0,  8,  12, 10, 14, 15, 17, 19, 21 ], #00
    [1,     1,      ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #01
    [ACP,   2,      3,  ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #02
    [ERR,   4,      ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR], #03
    [ACP,   4,      ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #04
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #05 OpA
    [ACP,   ACP,    ACP,ACP,7,  ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #06
    [7,     7,      7,  5,  6,  ACP, 7,  7,  7, ACP,ACP,ACP,ACP,ACP], #07
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP, 9, ACP,ACP,ACP,ACP,ACP,ACP], #08 <,>
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #09 >=, <=
    [10,    10,     10, 10, 10, ERR,10, 10, 11, 10 , 10, 10, 10, 10], #10
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #11
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,13, ACP,ACP,ACP,ACP,ACP,ACP], #12 Ops
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #13 OpR
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #14 Del
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP, 16,ACP,ACP,ACP], #15 | OpL
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #16 || OpL
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP, 18,ACP,ACP], #17 & OpL
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #18 && and OpL
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP, 20,ACP,ACP,ACP,ACP,ACP,ACP], #19 ! not OpL
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP], #20 != not equal OpR
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP, 22], #21 * OpA
    [ACP,   ACP,    ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP,ACP]  #22 ** OpA
]

#mapa de tipos
tiposTab = {"E=E":'', "A=A":'', "D=D":'', "L=L":'', "D=E":'',
            "E+E":'E', "E+D":'D', "D+E":'D', "D+D":'D', "A+A":'A',
            "E-E":'E', "E-D":'D', "D-E":'D', "D-D":'D',
            "E*E":'E', "E*D":'D', "D*E":'D', "D*D":'D',
            "E/E":'D', "E/D":'D', "D/E":'D', "D/D":'D',
            "E%E":'E', "-E":'E', "-D":'D',
            "L&&L":'L', "LyL":'L', "L||L":'L',"LoL":'L', "!L":'L',
            "E>E":'L', "D>E":'L', "E>D":'L', "D>D":'L',
            "E<E":'L', "D<E":'L', "E<D":'L', "D<D":'L',
            "E>=E":'L', "D>=E":'L', "E>=D":'L', "D>=D":'L',
            "E<=E":'L', "D<=E":'L', "E<=D":'L', "D<=D":'L',
            "E!=E":'L', "D!=E":'L', "E!=D":'L', "D!=D":'L', "A!=A":'L',
            "E==E":'L', "D==E":'L', "E==D":'L', "D==D":'L', "A==A":'L' }

tabSim = {}

tabFunc = {}

dim = '0'

def regtabSim(key, data):
    global tabSim
    tabSim[key]=data


def leetabSim(nombre):
    global tabSim, reng, colu
    if nombre in tabSim:
        return tabSim[nombre]
    else:
        erra(reng, colu, 'Error de Semantica', f'Identificador {nombre} no declarado', lex)
        return None


def erra(rn, cl, tipE, desE, strE):
    global errB
    errB = True
    cl = max(cl, 1)
    print(f"[{rn}] [{cl}] {tipE}: {desE}: {strE}")


def colCar(s):
    if s.isalpha()              : return 0
    if s.isdigit()              : return 1
    if s == '.'                 : return 2
    if s in ['+', '-', '%']     : return 3
    if s == '/'                 : return 4
    if s == '\n'                : return 5
    if s in ['<', '>']          : return 6
    if s == '='                 : return 7
    if s == '"'                 : return 8
    if s in ['{', '}', '(', ')',
             '[', ']', ',', ':', ';']: return 9
    if s == '|'                 : return 10
    if s == '&'                 : return 11
    if s == '!'                 : return 12
    if s == '*'                 : return 13
    #erra('Error Lexico', 'Simbolo No valido', s)
    return ERR

def scanner():
    global ERR, ACP, matran, idx, entrada, reng, colu
    estado = 0
    lexema = ''
    lex = ''
    tok = ''
    while idx < len(entrada) and estado != ERR \
          and estado != ACP:
        c = entrada[idx]
        idx = idx + 1
        while estado == 0 and c in ['\n', '\t', ' ']:
            c = entrada[idx]
            if c == '\n': 
                reng = reng + 1
                colu = 0
            else: colu = colu + 1
            idx = idx + 1

        if estado == 0 and not(c in ['\n', '\t', ' ']):
            idx = idx - 1

        while estado == 7 and c != '\n':
            c = entrada[idx]
            idx = idx + 1
            
        if estado in [7] and c == '\n':
            idx = idx - 1

        if estado in [11]:
            idx = idx - 1
        if estado == 7 or estado == 0 or estado == 11:
           if c == '\n':
               reng = reng + 1
               colu = 0
           else: colu = colu + 1
           c = entrada[idx]
           idx = idx + 1
        elif c == '\n':
            reng = reng + 1
            colu = 0
        elif c != '\n': colu = colu + 1

        col = colCar( c )
        if estado == 10 and not(c in ['\n', '"']):
            col = 1
        if col >= 0 and col <= 14:
            estAnt = estado
            estado = matran[estado][col]
            if estado in [ERR, ACP]: 
                idx = idx - 1
                break
            else: lexema = lexema + c
        else: break

    if not(estado in [ERR, ACP]): estAnt = estado
    if estAnt == 1: 
        lex = lexema
        tok = "Ide"
        if   lexema in palRes: tok = 'Res'
        elif lexema in cteLog: tok = 'CtL' 
    elif estAnt == 2: 
        lex = lexema
        tok = 'Ent'
    elif estAnt == 4: 
        lex = lexema
        tok = 'Dec'
    elif estAnt in [5, 6, 21, 22]: 
        lex = lexema
        tok = 'OpA'
    elif estAnt == 7:
        lex = ''
        tok = 'Com'
    elif estAnt == 11:
        lex = lexema
        tok = 'CtA'
    elif estAnt == 12:
        lex = lexema
        tok = 'OpS'
    elif estAnt in [8, 9, 13, 20]:
        lex = lexema
        tok = 'OpR'
    elif estAnt == 14: 
        tok = 'Del'
        lex = lexema
    elif estAnt == 3: 
        erra(reng, colu, 'Error Lexico', 
                           'Constante decimal incompleta', lexema)
        tok = 'Dec'
        lex = lexema
    elif estAnt == 10: 
        erra(reng, colu, 'Error Lexico', 
                           'Constante Alfabetica SIN cerrar', lexema)
        tok = 'CtA'
        lex = lexema

    elif estAnt in [15, 16, 17, 18, 19]:
        tok = 'OpL'
        lex = lexema    

    return tok, lex

def lexico(): 
    tok, lex = scanner()
    while tok == 'Com':
        tok, lex = scanner()

    return tok, lex

def importar():
    global tok, lex, reng, colu
    #print(tok, '\t\t', lex)
    tok, lex = lexico()
    if tok != 'CtA' and lex != '(':
       erra(reng, colu,'Error de Sintaxis', 'Se esperaba nombre de libreria o grupo libs y llego', lex)
    if lex == '(': #gpoLibs()
        tok, lex = lexico()
        while tok == 'CtA':
            tok, lex = lexico()
        if lex != ')':
            erra('Error de Sintaxis', 'Se esperaba ")" y llego', lex)
    tok, lex = lexico()

def varsconsts(): 
    global tok, lex, dim, clase, reng, colu, bDim
    
    tipo_valor = ''
    if lex == 'var'    :    clase = 'V'
    elif lex == 'const':    clase = 'C'
    tok, lex = lexico()
    if tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Ide y llego', lex)
    nomIde = lex
    tipo = 'I'
    tok, lex = lexico()
    if lex == '[': dimen()
    if not(lex in ['alfabetico', 'decimal', 
                   'entero', 'logico']):
        erra(reng, colu, 'Error de Sintaxis', 
            'Se esperaba tipo de dato y llego', lex)
    elif lex == 'alfabetico': tipo = 'A'
    elif lex == 'logico'    : tipo = 'L'
    elif lex == 'entero'    : tipo = 'E'
    elif lex == 'decimal'   : tipo = 'D'
    regtabSim(nomIde, [clase, tipo, dim, '0'])
    tok, lex = lexico()
    if lex == '=':
        tok, lex = lexico()
        if lex == '{': 
            gpoctes()
            regtabSim(nomIde, [clase, tipo, dim, '0'])
            dim = '0'
        else:
            if bDim == True:
                erra(reng, colu,'Error de Semantica',
                'La variable está dimensionada pero recibe valores incompatibles ', lex)
            insCodigo(['LIT',lex,'0'])
            insCodigo(['STO','0',nomIde])
            if   tok == 'CtA': tipo_valor = 'A'
            elif tok == 'CtL': tipo_valor = 'L'
            elif tok == 'Ent': tipo_valor = 'E'
            elif tok == 'Dec': tipo_valor = 'D'
            else:
                erra(reng, colu, 'Error de Sintaxis', 
                       'Se esperaba constante y llegó', lex)
                return
            if tipo_valor != tipo:
                erra(reng, colu, 'Error de Semantica', 
                       f'Se esperaba {tipo} y llego {tipo_valor}', lex)  
            
            tok, lex = lexico()
    if bDim == True: 
        bDim = False
   
    if lex == ',': varsconsts()


def dimen():
    global tok, lex, reng, colu, tabSim, bDim
   
    bDim = True
  
    tok, lex = lexico()
    if tok == 'Ide':
        simbolo = leetabSim(lex)
        if simbolo: 
            if simbolo[0] != 'C':  
                erra(reng, colu, 'Error de Semantica', 
                     'El Ide de la dimensión debe ser una constante declarada', lex)
                return
            elif simbolo[1] != 'E':
                erra(reng, colu, 'Error de Semantica', 
                     'El Ide en la dimension debe ser entero', lex)
                return
    elif tok != 'Ent': 
        erra(reng, colu, 'Error de Sintaxis', 
             'Se esperaba Ide o Ent y llegó', lex)
        return 
    tok, lex = lexico()       
    if lex != ']': 
        erra(reng, colu, 'Error de Sintaxis', 
             'Se esperaba "]" y llegó', lex)
        return
    tok, lex = lexico()
    if lex == '=':
        asigna()  
    

def gpoctes():
    global tok, lex, reng, colu, dim, bDim
    
    if bDim == False:
        erra(reng, colu,'Error de Semantica', 'La variable no está dimensionada para aceptar valores como un arreglo ', lex)
    dim = dim = str(int(dim) + 1)
    tok, lex = lexico()
    while lex != '}':
        if lex == '-':
            tok, lex = lexico()    
        if tok not in ['CtA', 'CtL', 'Ent', 'Dec']:
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba una constante y llegó', lex)
            return
        tok, lex = lexico()
        if lex == ',':
            dim = dim = str(int(dim) + 1)
            tok, lex = lexico()
            if lex == '-':
                tok, lex = lexico() 
            if tok not in ['CtA', 'CtL', 'Ent', 'Dec']:
                erra(reng, colu,'Error de Sintaxis', 'Se esperaba una constante y llegó', lex)
                return    
        elif lex != '}':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba "," o "}" y llego', lex)
            return    
    tok, lex = lexico()


def pars():
    global tok, lex, reng, colu
   
    firma = []
    while lex != ')':
        if tok != 'Ide':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba un identificador y llegó', lex)
            return
        nombre_parametro = lex
        tok, lex = lexico()
        if lex in ['entero', 'decimal', 'logico', 'alfabetico']:
            tipo_parametro = lex
            firma.append((nombre_parametro, tipo_parametro))
        else:
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba un tipo de dato y llegó', lex)
            return
        tok, lex = lexico()
        if lex == ',':
            tok, lex = lexico()
        elif lex != ')':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba una coma o ")" y llegó', lex)
            return
       
    return firma 
        
def termino():
    global tok, lex, reng, colu, nomIde, Operacion
    
    if lex == '(':
        tok, lex = lexico()
        expr()
        if lex != ')':
            erra(reng, colu,'Error de sintaxis', 'se esperaba ) y llego', lex)
        tok, lex = lexico()
    elif tok == 'CtA' or tok == 'CtL' or tok == 'Dec' or tok == 'Ent':
        if tok == 'CtA': pTipos.append('A')
        if tok == 'CtL': pTipos.append('L')
        if tok == 'Dec': pTipos.append('D')
        if tok == 'Ent': pTipos.append('E')
        if tok == 'CtL':
            if lex == 'verdadero':
                cte = 'V'
            elif lex == 'falso':
                cte = 'F'
        else:
            cte = lex
        insCodigo(['LIT', cte, '0'])
        if Operacion == '+':
            Operacion = ''
            insCodigo(['OPR','0', '2'])
            

        if Operacion == '-':
            Operacion = ''
            insCodigo(['OPR','0', '3'])
            

        if Operacion == '*':
            Operacion = ''
            insCodigo(['OPR','0', '4'])
            

        if Operacion == '/':
            Operacion = ''
            insCodigo(['OPR','0', '5'])
            

        if Operacion == '%':
            Operacion = ''
            insCodigo(['OPR','0', '6'])
          

        if Operacion == '^':
            Operacion = ''
            insCodigo(['OPR','0', '7'])
       
        
        if Operacion == '-u':
            Operacion = ''
            insCodigo(['OPR','0', '8'])
            

        if Operacion == '<':
            Operacion = ''
            insCodigo(['OPR','0', '9'])
            

        if Operacion == '>':
            Operacion = ''
            insCodigo(['OPR','0', '10'])
           

        if Operacion == '<=':
            Operacion = ''
            insCodigo(['OPR','0', '11'])
            

        if Operacion == '>=':
            Operacion = ''
            insCodigo(['OPR','0', '12'])
            
        
        if Operacion == '!=':
            Operacion = ''
            insCodigo(['OPR','0', '13'])
           

        if Operacion == '==':
            Operacion = ''
            insCodigo(['OPR','0', '14'])
           

        if Operacion == 'y':
            Operacion = ''
            insCodigo(['OPR','0', '15'])
            

        if Operacion == 'o':
            Operacion = ''
            insCodigo(['OPR','0', '16'])
            

        if Operacion == 'no':
            Operacion = ''
            insCodigo(['OPR','0', '17'])
         
        tok, lex = lexico()
        
    elif tok == 'Ide':
        nomIde = lex
        data = leetabSim(nomIde)
        if data != []:
            tipo = data[1]
        else: tipo = 'I'
        pTipos.append(tipo) 
        insCodigo(['LOD', nomIde, '0'])

        if Operacion == '+':
            Operacion = ''
            insCodigo(['OPR','0', '2'])
          

        if Operacion == '-':
            Operacion = ''
            insCodigo(['OPR','0', '3'])
         

        if Operacion == '*':
            Operacion = ''
            insCodigo(['OPR','0', '4'])
          

        if Operacion == '/':
            Operacion = ''
            insCodigo(['OPR','0', '5'])
          

        if Operacion == '%':
            Operacion = ''
            insCodigo(['OPR','0', '6'])
           

        if Operacion == '^':
            Operacion = ''
            insCodigo(['OPR','0', '7'])
          
        
        if Operacion == '-u':
            Operacion = ''
            insCodigo(['OPR','0', '8'])
         

        if Operacion == '<':
            Operacion = ''
            insCodigo(['OPR','0', '9'])
          

        if Operacion == '>':
            Operacion = ''
            insCodigo(['OPR','0', '10'])
        

        if Operacion == '<=':
            Operacion = ''
            insCodigo(['OPR','0', '11'])
           

        if Operacion == '>=':
            Operacion = ''
            insCodigo(['OPR','0', '12'])
           
        
        if Operacion == '!=':
            Operacion = ''
            insCodigo(['OPR','0', '13'])
           

        if Operacion == '==':
            Operacion = ''
            insCodigo(['OPR','0', '14'])
           

        if Operacion == 'y':
            Operacion = ''
            insCodigo(['OPR','0', '15'])
           

        if Operacion == 'o':
            Operacion = ''
            insCodigo(['OPR','0', '16'])
           

        if Operacion == 'no':
            Operacion = ''
            insCodigo(['OPR','0', '17'])
           

        tok, lex = lexico()
        if lex == '(':
            lfunc()
        elif lex == '[':
            dimen()
         


def signo():
    global tok, lex
   
    if lex == '-':
        tok, lex = lexico()
    termino()
    

def expo():
    global tok, lex, pTipos
   
    op = '^'
    while op == '^':
        op =''
        signo()
        if lex == '^':
            op = lex
            tok, lex = lexico()
      

def multi():
    global tok, lex, pTipos, reng, colu, Operacion
    
    op = '*'
    bOp = False
    while op in ['*', '/', '%']:
        op =''
        expo()
        if bOp:
    
            bOp = False
            tRes = ''
            kTipo = pTipos.pop()
            kTipo = pTipos.pop() + kTipo
            kTipo = pTipos.pop() + kTipo
            try:            
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                pTipos.append(tRes)

        if lex in ['*', '/', '%']:
            op = lex
            bOp = True
            pTipos.append(op)

            if op == '*': Operacion = '*'
            if op == '/': Operacion = '/'
            if op == '%': Operacion = '%'
            tok, lex = lexico()
    

def suma():
    global tok, lex, pTipos, reng, colu, Operacion
    
    op = '+'
    bOp = False
    while op in ['+', '-']:
        op = ''
        multi()
        if bOp:
    
            bOp = False
            tRes = ''
            kTipo = pTipos.pop()
            kTipo = pTipos.pop() + kTipo
            kTipo = pTipos.pop() + kTipo
            try:            
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                pTipos.append(tRes)
        
        if lex in ['+', '-']:
            op = lex
            bOp = True
            pTipos.append(op)

            if op == '+': Operacion = '+'
            if op == '-': Operacion = '-'
            tok, lex = lexico()
    

def oprel():
    global tok, lex, pTipos, reng, colu, Operacion
   
    op = '<'
    bOp = False
    while op in ['<', '>', '<=', '>=', '!=', '==']:
        op = ''
        suma()
        if bOp:
   
            bOp = False
            tRes = ''
            kTipo = pTipos.pop()
            kTipo = pTipos.pop() + kTipo
            kTipo = pTipos.pop() + kTipo
            try:            
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                pTipos.append(tRes)

        if lex in ['<', '>', '<=', '>=', '!=', '==']:
            op = lex
            bOp = True
            pTipos.append(op)
            if op == '<': Operacion = '<'
            if op == '>': Operacion = '>'
            if op == '<=': Operacion = '<='
            if op == '>=': Operacion = '>='
            if op == '!=': Operacion = '!='
            if op == '==': Operacion = '=='
            tok, lex = lexico()
   

def opno():
    global tok, lex 
   
    if lex == 'no':
        tok, lex = lexico()
    oprel()   
   

def opy():
    global tok, lex, pTipos, reng, colu, Operacion
   
    op = 'y'
    bOp = False
    while op in ['y', '&&']:
      op = ''
      opno()
      if bOp:
   
            bOp = False
            tRes = ''
            kTipo = pTipos.pop()
            kTipo = pTipos.pop() + kTipo
            kTipo = pTipos.pop() + kTipo
            try:            
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                pTipos.append(tRes)

      if lex in ['y', '&&']:
         op = lex
         bOp = True
         pTipos.append(op)

         if op in ['y', '||']: Operacion = 'y'
         tok, lex = lexico()
   

def expr():
    global tok, lex, pTipos, reng, colu, Operacion
   
    op = 'o'
    bOp = False
    while op in ['o', '||']:
      op = ''
      opy()
      if bOp:
   
            bOp = False
            tRes = ''
            kTipo = pTipos.pop()
            kTipo = pTipos.pop() + kTipo
            kTipo = pTipos.pop() + kTipo
            try:            
                tRes = tiposTab[kTipo]
            except KeyError:
                erra(reng, colu,'Error de Semantica', 'conflicto en el tipo de operador', kTipo)
                tRes = 'I'
            if tRes != '':
                pTipos.append(tRes)

      if lex in ['o', '||']:
         op = lex
         bOp = True
         pTipos.append(op)
         if op in ['o', '||']: Operacion = 'o'
         tok, lex = lexico()
   

def fmtleer():
    global tok, lex, reng, colu
   
    if lex == 'Leer':
        tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    if tok != 'Ide':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    else:
        insCodigo(['OPR', lex, '19'])
    tok, lex = lexico()
    if lex == '[': udim()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    tok, lex = lexico()
   

def udim():
    global tok, lex, reng, colu
   
    tok, lex = lexico()
    expr()
    if lex != ']':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    tok, lex = lexico()
   

def fmtimprime():
    global tok, lex, bImp, reng, colu
   
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    sp = ','
    while sp == ',':
        tipo = 'A'
        if pTipos != []:
            tipo = pTipos.pop()
        if tipo not in ['E', 'D', 'L', 'A']:
            erra(reng, colu,'Error de Semantica', 'tipo en imprime NO valido', tipo)
        sp = ''
        expr()
        sp = lex
        if sp == ',':
            insCodigo(['OPR', '0', '20'])
            tok, lex = lexico()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ) y llego', lex)
    cImp = '20'
    if bImp: cImp = '21'
    insCodigo(['OPR', '0', cImp])
    tok, lex = lexico()
   
    
def comando():
    global tok, lex, bImp, reng, colu, variable
   
    if lex == 'fmt':
        tok, lex = lexico()
        if lex != '.':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba . y llegó', lex)
        tok, lex = lexico()
        if lex == 'Imprime': 
            fmtimprime()
        elif lex == 'Imprimenl':
            bImp = True
            fmtimprime()
        elif lex == 'Leer':
            fmtleer()
        elif lex == 'Lmp': fmplmp()
        else:
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba función de fmt [Leer, Imprime, Imprimenl] y llegó', lex)
    elif tok == 'Ide': 
    
        variable = lex
        if lex == '(':
            lfunc
        elif lex == '[':  
            dimen()
        else:  
            asigna()
    elif lex in ['si', 'desde', 'regresa', 'interrumpe', 'continua']:  
        instruccion()
    else:
        bloque()
    

def fmplmp():
    global tok, lex, reng, colu
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
    tok, lex = lexico()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba Identificador y llego', lex)
    insCodigo(['OPR','0','18'])
    tok, lex = lexico()
   


def desde():
    global tok, lex, reng, colu, bCiclo
    bCiclo = True
    
    
    tok, lex = lexico()
    if lex == '{':
        bloque()
    
        return
    if tok == 'Ide':  
        asigna()
    if lex != ';':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ";" después de la inicialización', lex)
        return
    tok, lex = lexico()
    expr()  
    if lex != ';':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ";" después de la condición', lex)
        return
    tok, lex = lexico()
    if tok == 'Ide':  
        asigna()
    if lex != '{':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba "{" y llego', lex)
        return
    tok, lex = lexico()
    while lex != '}': 
        if lex == 'desde':
            desde()
        else:
            comando()
    if lex != '}':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba "}" y llego', lex)
        return
    bCiclo = False
  
    tok, lex = lexico()
    

   
def asigna():
    global tok, lex, reng, colu, variable
    tok, lex = lexico()
   
    if lex == '[':
        udim()  
        tok, lex = lexico()
   
    if lex == '=':
        tok, lex = lexico()
    expr()
   
    insCodigo(['STO','0',variable])
    variable = ''
   

def regresa():
    global tok, lex, reng, colu, pRetorno, bRetorno, bRegresa
   
    Tipo = ''
    NTipo = ''
    if not bRetorno:
        erra(reng, colu,'Error de Semantica', 'La funcion no espera', lex)
        return
    bRegresa = True
   
    if lex == 'regresa':
        tok, lex = lexico()
    
        if tok == 'Ent':Tipo = 'E'
        if tok == 'Dec':Tipo = 'D'
        if tok == 'CtL':Tipo = 'L'
        if tok == 'CtA':Tipo = 'A'
        if tok == 'Ide':
            nomIde = lex
            dato = leetabSim(nomIde)
            if dato:
                Tipo = dato[1]
        if Tipo == 'A': NTipo = 'alfabetico'
        if Tipo == 'E': NTipo = 'entero'
        if Tipo == 'D': NTipo = 'decimal'
        if Tipo == 'L': NTipo = 'logico'
    
        if pRetorno[0] =='A':
            if Tipo != pRetorno[0]:
                erra(reng, colu,'Error de Semantica', 'Tipo de retorno no valido, se esperaba alfabetico y llego', NTipo)
        if pRetorno[0] =='E':
            if Tipo != pRetorno[0]:
                erra(reng, colu,'Error de Semantica', 'Tipo de retorno no valido, se esperaba entero y llego', NTipo)
        if pRetorno[0] =='D':
            if Tipo != pRetorno[0]:
                erra(reng, colu,'Error de Semantica', 'Tipo de retorno no valido, se esperaba decimal y llego', NTipo)
        if pRetorno[0] =='L':
            if Tipo != pRetorno[0]:
                erra(reng, colu,'Error de Semantica', 'Tipo de retorno no valido, se esperaba logico y llego', NTipo)

        expr()
    
        if lex != '}':
            erra(reng, colu,'Error de Sintaxis', 'se esperaba } y llegó', lex)
            return
    

def si():
    global tok, lex, reng, colu
   
    tok, lex = lexico()
    expr()
    if lex != '{':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba "{" y llegó', lex)
        return
    bloque()
    if lex == 'sino':
    
        tok, lex = lexico()
        expr()
        if lex != '{':
            erra(reng, colu,'Error de Sintaxis', 'Se esperaba "{" y llegó', lex)
            return
        bloque()
    
        
def interrumpe():
    global tok, lex, reng, colu, bCiclo
   
    if bCiclo == False:
        erra(reng, colu,'Error de Semantica','interrumpe fuera de ciclo', tok)
    tok, lex = lexico()
    if lex == 'interrumpe':
        tok, lex = lexico()
    

def continua():
    global tok, lex, reng, colu, bCiclo
    if bCiclo == False:
        erra(reng, colu,'Error de Semantica','continua fuera de ciclo', tok)
   
    tok, lex = lexico()
    if lex == 'continua':
        tok, lex = lexico()       
    

def instruccion():
    global tok, lex, reng, colu
   
    if lex == 'si':
        si() 
    elif lex == 'desde':
        desde()
    elif lex == 'regresa':
        regresa()
    elif lex == 'interrumpe':
        interrumpe()
    elif lex == 'continua':
        continua()
    else:
        erra(reng, colu,"Error de Sintaxis", "Se esperaba una instrucción válida y llegó", lex)
    
        
def lfunc():
    global tok, lex, reng, colu, conEtiq
  
    tok, lex = lexico()
    sm = lex
    etiq = '_E' + str(conEtiq)
    conEtiq = conEtiq+1
    insCodigo(['LOD', etiq, '0'])
    while sm != ')':
        expr()
        sm = lex
        if lex == ',':
            tok, lex = lexico()
    insCodigo(['CAL',nomIde,'0'])
    regtabSim(etiq, ['I', 'I', str(conLin), '0'])
   
    expr()
    while lex == ',':
        tok, lex = lexico()
        expr()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ")" y llego', lex)
        return
    tok, lex = lexico()
   

def estatutos():
    global tok, lex, reng, colu
   
    while lex != '}':  
        comando()  
   
   

def bloque():
    global tok, lex, reng, colu
   
    if lex == 'func':
        funciones()
    if lex != '{':  
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba { y llegó', lex)
    tok, lex = lexico()
    estatutos()  
    if lex != '}':  
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba } y llegó', lex)
    tok, lex = lexico()
   
    
def funciones():
    global tok, lex, reng, colu, tabFunc, bRetorno, pRetorno
    
    pRetorno = []
    nombre_func = None
    firma_func = []
    nombre_func = lex
    
    for key, value in tabSim.items():
        print(f"'{key}': {value}")
    tok, lex = lexico()
    if lex == 'principal':
        nombre_func = lex
        if nombre_func in tabFunc:
            erra(reng, colu,'Error de Semántica',
                f'Función principal ya existe', nombre_func)
            return
        tabFunc[nombre_func] = []
    elif tok == 'Ide':
        nombre_func = lex
    else:
        erra(reng, colu,'Error de Sintaxis',
            'Se esperaba nombre de funcion y llego', lex)
        return
    if tok == 'Res' and nombre_func == 'principal':
        regtabSim('_P', ['I', 'I', '1', '0'])
    tok, lex = lexico()
    if lex != '(':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ( y llego', lex)
        return
    tok, lex = lexico()
    if lex != ')': 
        firma_func = pars()
    if lex != ')':
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba ) y llego', lex)
        return
    if nombre_func != 'principal':
        if nombre_func in tabFunc:
            if any(firma_func == firma for firma in tabFunc [nombre_func]):
                erra(reng, colu,'Error de Semantica',
                    f'Funcion {nombre_func} ya existe con la misma firma', str(firma_func))
                return
        if nombre_func not in tabFunc:
            tabFunc[nombre_func] = []
        tabFunc[nombre_func].append(firma_func)
    tok, lex = lexico()
    if lex in ['alfabetico','decimal', 'entero', 'logico']:
        bRetorno = True
    
    
        may = lex.upper()
        tipo = may[0]
        if nomIde != 'principal':
            regtabSim(nombre_func, ['F', tipo, str(conLin), '0'])
        if lex == 'alfabetico': pRetorno.append('A')
        if lex == 'decimal'   : pRetorno.append('D')
        if lex == 'entero'    : pRetorno.append('E')
        if lex == 'logico'    : pRetorno.append('L')    
    
        tok, lex = lexico()
    if lex == '{':
        regtabSim(nombre_func, ['F', 'I', str(conLin), '0'])
        bloque()
        if bRetorno and not bRegresa:
            tipoEsperado = (
                'alfabetico' if pRetorno[0] == 'A' else
                'decimal'    if pRetorno[0] == 'D' else
                'entero'     if pRetorno[0] == 'E' else
                'logico'     if pRetorno[0] == 'L' else 'desconocido'
            )
            erra(reng, colu, 'Error de Semantica',
                 f'Se esperaba regresa de tipo {tipoEsperado}', lex)

        if nombre_func  == 'principal':
            insCodigo(['OPR', '0', '0'])
        else:
            insCodigo(['OPR', '0', '1'])
    else:
        erra(reng, colu,'Error de Sintaxis', 'Se esperaba { y llego', lex)
    
    if lex == 'func':
        funciones()
    
        
def prgm():
    global entrada, idx, errB, tok, lex, archE
    archE = ''
    print(archE[len(archE)-3:])
    while (archE[len(archE)-3:] != 'icc'):
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        if archE == '.': exit(0)
        aEnt = None
        try:
            aEnt = open(archE, 'r+')
            break
        except FileNotFoundError:
            print(archE, 'No exite volver a intentar')
    
    if aEnt != None:
        while (linea := aEnt.readline()):
            entrada += linea
        aEnt.close()

    print('\n\n' + entrada + '\n\n')  
    #while idx < len(entrada):
    idx = 0
    errB = False
    tok, lex = lexico()
    #print(tok, '\t\t', lex)
    while lex == 'importar':
        importar()

    while lex in ['var', 'const']:
        varsconsts()    

    funciones()
    if not(errB):
        print(archE, 'Compilo con EXITO!!!')

if __name__ == '__main__':
    prgm()
    if not (errB):
        archS = archE [0:len(archE)-3] + 'eje'
        try:
            #print(archS)
            with open(archS, 'w') as aSal:
                for x, y in tabSim.items():
                    aSal.write(x + ',')
                    aSal.write(y[0]+',')
                    aSal.write(y[1]+',')
                    aSal.write(str(y[2])+',')
                    aSal.write(str(y[3])+',')
                    aSal.write('#,\n')
                aSal.write('@\n')
                for x, y in progm.items():
                    aSal.write(str(x) + ' ')
                    aSal.write(y[0] + ' ')
                    aSal.write(y[1] + ', ')
                    aSal.write(y[2] + '\n')
                aSal.close
        except FileNotFoundError:
            print(archE, 'No existe volver a intentar')