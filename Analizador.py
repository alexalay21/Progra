#-*-encoding:utf8-*-

class analizador_texto:
    def __init__(self):
        self.letra_actual = ''
        self.estado_actual = 0
        self.valor_lexema = ''
        self.operadores = ['+','-','*','x','.','^']
        self.puntuacion = [',',':',';','.']
        self.aceptacion = True
        self.reservadas = ['teorema','Teorema','matematico','matematica',
        'Hilbert','Turing','analisis','Euler','Fermat','Pitágoras','automata','Boole',
        'Cantor','Perelman','experimentacion','fisico','fisica',
        'Astronomia','Mecanica','Newton','Einstein','Galileo','Modelo',
        'Tesla','Dinamica','Particulas',]

    def switch(self, estado):
        self.estados = {
            0: self.s0,
            1: self.s1,
            2: self.s2,
            3: self.s3,
            4: self.s4,
            5: self.s5,
            6: self.s6,
            7: self.s7,
            8: self.s8,
            9: self.s9,
            10: self.s10,
            11: self.s11,
            12: self.s12,
            13: self.s13,
            14: self.s14,
            15: self.s15,
            16: self.s16,
        }

        func = self.estados.get(estado, lambda: 'CARACTER NO VALIDO')
        return func()

    def valuar_dato(self, dato):
        try:
            int(dato)
            return True
        except ValueError:
            return False
    
    def s0(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 1
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
    
    def s1(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 2
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def s2(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[4]:
                self.estado_actual = 3
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[2] or str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'NUMERO ENTERO'
                self.aceptacion = False
            elif str(self.letra_actual) in self.puntuacion:
                print 'NUMERO ENTERO'
                self.aceptacion = False
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 2
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True
        
    def s3(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 6
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def s4(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 1:
                self.estado_actual = 7
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def s5(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >=0:
                self.estado_actual = 8
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def s6(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[0] or str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 5
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == self.operadores[2] or str(self.letra_actual) == self.operadores[3]:
                self.estado_actual = 4
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == ' ':
                print 'NUMERO REAL'
                self.aceptacion = False
            elif str(self.letra_actual) in self.puntuacion:
                print 'NUMERO REAL'
                self.aceptacion = False
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 6
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True
    
    def s7(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) == 0:
                self.estado_actual = 9
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def s8(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[4]:
                self.estado_actual = 10
                self.valor_lexema = self.valor_lexema + self.letra_actual
            elif str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.estado_actual = 8
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def s9(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == self.operadores[5]:
                self.estado_actual = 12
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual   
        else:
            self.aceptacion = False
            print 'NO SE RECONOCE LA CADENA'

    def s10(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def s11(self):
        if self.valuar_dato(self.letra_actual) == False:
            if str(self.letra_actual) == ' ':
                print 'NUMERO COMPLEJO'
                self.aceptacion = False
            elif str(self.letra_actual) in self.puntuacion:
                print 'NUMERO COMPLEJO'
                self.aceptacion = False
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
        else:
            self.aceptacion = False
            print 'NO SE RECONOCE LA CADENA'
    
    def s12(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self. letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            if str(self.letra_actual) == self.operadores[1]:
                self.estado_actual = 15
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def s13(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 13
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            if str(self.letra_actual) == 'i':
                self.estado_actual = 11
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
    
    def s14(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            if str(self.letra_actual) == ' ':
                print 'NOTACION CIENTIFICA'
                self.aceptacion = False
            elif str(self.letra_actual) in self.puntuacion:
                print 'NOTACION CIENTIFICA'
            else:
                self.estado_actual = 16
                self.valor_lexema = self.valor_lexema + self.letra_actual
            
    def s15(self):
        if self.valuar_dato(self.letra_actual) == True:
            if int(self.letra_actual) >= 0:
                self.estado_actual = 14
                self.valor_lexema = self.valor_lexema + self.letra_actual
            else:
                self.aceptacion = False
                print 'NO SE RECONOCE LA CADENA'
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual

    def s16(self):
        if str(self.letra_actual) == ' ':
            if self.valor_lexema in self.reservadas:
                print 'PALABRA RESERVADA'
                self.aceptacion = False
            elif str(self.letra_actual) in self.puntuacion:
                print 'CADENA'
                self.aceptacion = False
            else:
                print 'CADENA'
                self.aceptacion = False
        else:
            self.estado_actual = 16
            self.valor_lexema = self.valor_lexema + self.letra_actual
            self.aceptacion = True

    def analiza(self, cadena):
        cadena = str(cadena)
        palabras = cadena.split()
        for i in palabras:
            self.aceptacion = True
            self.valor_lexema = ""
            self.estado_acutal = 0
            i = i + ' '
            for x in i:
                if self.aceptacion == True:
                    self.letra_actual = x
                    self.switch(self.estado_actual)

p=analizador_texto().analiza(raw_input('Cadena: '))
while p!='':
    analizador_texto().analiza(raw_input('Cadena: '))
