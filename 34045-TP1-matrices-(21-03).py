# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:06:19 2023

@author: casti
"""

class myarray1():
    '''
    Condiciones
    -----------
    Las matrices se van a indexar de forma matemática, es decir que tanto filas
    como columnas empiezan en el número 1.
    
    El número de filas x columna debe coincidir con el largo de la lista elems.
    '''
    def __init__(self, elems, r, c, by_row):
        
        if len(elems) != r*c:
            
            print(f'Error: Las filas por columnas ({r*c}) no coincide \ncon el largo de la lista ({len(elems)}).')
            
        else:
            self.elems=elems
            self.r=r
            self.c=c
            self.by_row=by_row
        
        
    def alt(self, contador=0):
        '''
        Se encarga de devolver la lista elems ingresada al objeto "myarray1" de 
        maneratal que vaya en orden por columna.
        
        Condición
        ---------
        No ingresar nada en contador dado que es usado de forma interno y tiene
        que empezar en cero.
        
        Esta función es de uso interno.
        Parameters
        ----------
        contador : int, optional
            El contador sirve para limitar el slicing sobre la lista y terminar
            con la recursividad. The default is 0.
            
        '''
        a=[]
        
        if contador == self.c:
            
            0
        else:
            
            a=self.elems[contador:len(self.elems):self.c]
            a+=self.alt(contador+1)
            
        return a
    
    def get_pos (self,j,k):
        '''
        Toma las coordenadas j,k en la matriz y devuelve la posicion m asociada 
        en la lista elems.
        
        No se hace chequeo del by_row porque si es falso no se modifica el tamaño de la matriz
        Condición
        ---------
        Las matrices se van a indexar de forma matemática, es decir que tanto filas
        como columnas empiezan en el número 1.
        
        Parameters
        ----------
        j : int
            Fila.
        k : TYPE
            Columna
            
        '''
        
        if j <= self.r and k <=self.c:
            
            n=j*self.c-(self.c-k)-1#le resto uno porque las posiciones empiezan de cero
            
            return n
        
        else:
            print(f'Los números ingresados estan fuera de rango, reingrese numeros menor que {self.r} en la fila y menor que {self.c} en la columna.')
    
    def get_coords(self,n):
        '''
        Toma una posición m en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz.
        
        No se hace chequeo del by_row porque si es falso no se modifica el tamaño de la matriz.
        
        Condición
        ---------
        La función esta realizada a partir del indexin de listas por lo que las 
        posiciones comienzan desde cero.
        
        Parameters
        ----------
        n : int
            Posición de la cual se buscan las coordenadas.
        '''
        if n < len(self.elems) and n >= 0:
            self.n=n
            a=0+self.n
            
            while a>0:
                
                a-=self.c
            
            if a < 0:
                a+=self.c
                
            k=(self.n+1)-len(self.elems[:n-a]) #le resto al n (n+1, porque las posicion es uno menos) le resto el nro de columnas enteras y me queda k 
            j=int((self.n+self.c-k+1)/self.c) #viene de despejar j de la funcion get_pos
            
            return (j,k)
        
        else:
            print(f'Error:El número {n} esta fuera de rango, de 0 a {len(self.elems)-1}')
    
    def switch(self):
        '''
        Devuelve un objeto con la misma matriz, pero alterando la lista elems y 
        cambiando el valor de verdad de by_row.
        
        Returns
        -------
        Type: myarray1
        
        '''
        
        m_inv=myarray1.alt(self)
        
        if self.by_row == False:
            
            by_who = True
            
        else:
            
            by_who = True
        
        return myarray1(m_inv, self.r, self.c, by_who)
    
    def get_row(self, j):
        '''
        Devuelve la fila j.
        
        Condición
        ---------
        j debe estar entre el número de filas de la matriz.
        Las filas se deben llamr en orden matemático por lque comienzan en 1
        
        Parameters
        ----------
        j : int
            Número de fila que se busca.
            
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
            
        if j in range(1,selfm.r+1):
            lista=selfm.elems[j*selfm.c-selfm.c:j*selfm.c]
        
            return myarray1(lista,1,self.c,True)
        
        else:
            print(f'Errror: Solo puedes ingresar números entre 1 y {self.r+1}.')
            
    def get_col(self,k):
        '''
        Devuelve la columna k
        
        Condición
        ---------
        k debe estar entre el número de columnas de la matriz.
        
        Las columnas se deben llamr en orden matemático por lque comienzan en 1
        
        Parameters
        ----------
        k : int
            Número de columna que se busca.
            
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
            
        if k in range(1,selfm.c+1):
            
            l=selfm.elems[k-1::selfm.c]
        
            return myarray1(l,self.r,1, True)
        
        else:
            
            print(f'Error: El número ingresado esta fuera de rango, ingresar entre 1 y {self.c+1}.')
        
    def get_elem (self,j,k):
        '''
        Devuelve el elemento de las coordenadas j,k.
        
        Condición
        ---------
        Las coordenadas debe estar entre el número de filas y columnas de la 
        matriz
        
        las filas y columnas se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila.
        k : int
            Columna.
            
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        
        if j <= selfm.r and k <= selfm.c and j>0 and k>0:
            
            lista=selfm.elems[j*selfm.c-selfm.c:j*selfm.c]
            
            return lista[k-1] #le resto uno porque las columnas empiezan de 1 y las posiciones de 0
        
        else:
            print(f'Los números ingresados estan fuera de rango, reingrese \nnumeros menor que {self.r} en la fila y menor que {self.c} en la columna.')

    
        
    def del_rowlista(self,j,fs=1, fila=0):
        '''
        Devuelve una matriz en formato de lista con la fila j eliminada.
        
        Condiciones
        -----------
        j debe estar entre el número de filas de la matriz.
        
        No ingresar nada en fs dado que es usado de forma interno y tiene que 
        empezar en uno.
        
        las filas a eliminar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila que se quiere eleminar.
        fs : TYPE, optional
            NO INGRESAR. The default is 1.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
            
        matriz=[]
        
        if fs > selfm.r  or j > selfm.r or j < 0:
            
            fila+=selfm.r-1
            
            if j > selfm.r or j < 0:
                print(f'Error: Solo puedes eliminar filas o columnas entre 1 y {self.r}')
            
        else:
            
            if j == fs:
                
                selfm.del_rowlista(j,fs+1)
            
            else:
                
                matriz=selfm.get_row(fs).elems
            
            matriz+=selfm.del_rowlista(j ,fs+1)
                
        return matriz
    
    def del_row(self,j):
        '''
        Devuelve un objeto de la clase con la fila j eliminada.
        
        Condiciones
        -----------
        j debe estar entre el número de filas de la matriz.
        
        las filas a eliminar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila que se quiere eleminar.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #------------------------------
        lista=selfm.del_rowlista(j)
        
        return myarray1(lista,selfm.r-1,selfm.c, selfm.by_row)
        
    def del_col(self, k):
        '''
        Devuelve un objeto de la clase con la columna k eliminada.
        
        Condiciones
        -----------
        k debe estar entre el número de filas de la matriz.
        
        las columnas a eliminar se deben llamar en órden matmático por lo que comienzan en 1.
        
        k : int
            Columna que se quiere eleminar.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #-----------------------
        return selfm.traspose().del_row(k).traspose()
    
    def swap_rows (self,j,k):
        '''
        Devuelve un objeto de la clase con la fila j en el lugar de la k y viceversa.
        
        Condiciones
        -----------
        j y k debe estar entre el número de filas de la matriz.
        
        las filas a intercambiar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila que se quiere intercambiar.
        k: int
            Fila que se quiere intercambiar.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
          
        #------------------------------------------------------
        if j in range(1,selfm.r+1) and k in range(1,selfm.r+1):
            listamod=selfm.elems.copy()
            
            listamod[0:selfm.c*max(j,k)]+=selfm.elems[min(j,k)*selfm.c-selfm.c:min(j,k)*selfm.c]
            listamod[0:selfm.c*min(j,k)]+=selfm.elems[max(j,k)*selfm.c-selfm.c:max(j,k)*selfm.c]
            
            return myarray1(listamod, selfm.r+2, selfm.c, selfm.by_row).del_row(min(j,k)).del_row(max(j,k))
        
        else: 
            print(f'Error: Alguna de sus filas esta fuera del rango, entre 1 y {self.r}.')
        
    def swap_cols(self,l,m):
        '''
        Devuelve un objeto de la clase con la columna l en el lugar de la m y viceversa.
        
        Condiciones
        -----------
        l y m debe estar entre el número de columnas de la matriz.
        
        las columnas a intercambiar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        l : int
            Columna que se quiere intercambiar.
        m: int
            Columna que se quiere intercambiar.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #--------------------------------------------------
        if l in range(1,selfm.c+1) and m in range(1,selfm.c+1):
            
            return selfm.traspose().swap_rows(l,m).traspose()
        else:
            print(f'Error: Alguna de sus columnas esta fuera del rango, entre 1 y {self.c}.')
    
    def scale_row(self,j,x):
        '''
        Devuelve un objeto de la clase con la fila j multiplicada por el número x.
        
        Condiciones
        -----------
        j debe estar entre el número de filas de la matriz.
        
        las filas a intercambiar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila que se quiere intercambiar.
        n: int
            Número por el que quiere multiplicar la fila ingresada.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #------------------------------------------------------------------- 
        if j in range(1, selfm.r+1):
            matriz=selfm.elems.copy()
            row=selfm.get_row(j).elems
            row_mul=[]
            
            for i in row:
                
                row_mul.append(i*x)
                
            matriz[j*selfm.c-selfm.c:j*selfm.c]=row_mul
            
            return myarray1(matriz,selfm.r, selfm.c, selfm.by_row)
        
        else:
            print(f'Error: La fila ingresada esta fuera del rango, entre 1 y {self.r}.')
    
    def scale_cols(self,k,y):
        '''
        Devuelve un objeto de la clase con la fila j multiplicada por el número x.
        
        Condiciones
        -----------
        j debe estar entre el número de filas de la matriz.
        
        las filas a intercambiar se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Fila que se quiere intercambiar.
        n: int
            Número por el que quiere multiplicar la fila ingresada.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #------------------------------------------------------------
        if k in range(1, selfm.c+1):
            return selfm.traspose().scale_row(k,y).traspose()
        
        else:
            print(f'Error: La columna ingresada esta fuera del rango, entre 1 y {self.r}.')
        
    
    
    def traspose (self):
        '''
        Traspone la matriz ingresada cambiando filas y columnas.

        Returns
        -------
        myarray2
            Nuevo objeto traspuesto al original.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #-------------------------------------------------------------
        return myarray1(selfm.switch().elems,selfm.c,selfm.r,selfm.by_row)
    
    
    def flip_rows(self):
        '''
        Devuelve las filas volteadas [1,2,3] ---> [3,2,1]

        Returns
        -------
        myarray2
            Nuevo objeto dónde las filas estan volteadas respecto al original.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #----------------------------------------
        lista=list(reversed(selfm.elems.copy()))
        matriz=[]
        
        for i in range(0, selfm.r):

            matriz+=lista[len(lista)-i*selfm.c-selfm.c:len(lista)-i*selfm.c]

        return myarray1(matriz,selfm.r,selfm.c, selfm.by_row)
        
    
    def flip_cols(self):
        '''
        Devuelve las filas volteadas [1,      [3,
                                      2,---->  2,
                                      3]       1]   

        Returns
        -------
        myarray2
            Nuevo objeto dónde las columnas estan volteadas respecto al original.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #--------------------------------------------
        return selfm.traspose().flip_rows().traspose()
    
    def shift (self, n, m):#n empieza de cero
        '''
        
        Devuelve una lista desplazar las filas cuantas veces se pida para arriba o para abajo.
        
        Condición
        ---------
        m debe decir ecplicitamente "arriba" o "abajo"
        
        Parameters
        ----------
        n: int
            Número de veces que se quiere desplazar las filas.
        m: str
            Dirección hacia dónde se desplaza la fila.
        '''
        
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #----------------------------------------------------------------------
        if m == 'arriba':
            lista=selfm.elems[selfm.c*n:selfm.c*selfm.c]+selfm.elems[0:selfm.c*n]
           
        elif m == 'abajo':
           
            lista=selfm.elems[len(selfm.elems)-selfm.c*n:selfm.c*selfm.c]+selfm.elems[0:len(selfm.elems)-selfm.c*n]
        
        else:
            print('Error: Solo puede ir para "arriba" o "abajo".')
            
        return myarray1(lista, selfm.r, selfm.c, selfm.by_row)
    
    
    def det(self):
        '''
        Saca el determinante de una matriz de nxn:
        
        Condición
        ---------
        La matriz tiene que ser cuadrada
        
        Returns
        -------
        determinante : int
            Determinante de la función.
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
        if self.c == self.r:
            determinante=0
            
            if len(selfm.elems) == 1:
                
                determinante=selfm.elems[0]
                
            else:
                
                for i in range(1,selfm.c+1):
                    
                    submatriz=selfm.del_row(1).del_col(i)
                    elemento=selfm.get_elem(1,i)
                    
                    determinante+=((-1)**i)*elemento*submatriz.det()
                    
            return determinante
        
        else:
            
            print('No se puede calcular el determinante de matrices que no son cuadradas.')
            
    def __add__(self,b):
        '''
        Realiza la suma entre matrices y matrices con números.
        
        Condición:
        ---------
        Las dos matrices ingresadas deben ser del mismo tamaño.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida = [n+b for n in selfm.elems]
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[selfm.elems[m]+b.elems[m] for m in range(0, len(b.elems))]
            else:
                print('No se pueden sumar dos matrices de distinto tamaño')
        else:
            print(f'No se puede sumar {type(self)} con {type(b)}.')
            
        return myarray1(salida, self.r, self.c, selfm.by_row)
    
    def __radd__(self,b):
        '''
        Realiza la suma entre matrices y números leyendo el primer argumento 
        como un numero real
        
        Condición:
        ---------
        Las dos matrices ingresadas deben ser del mismo tamaño.

        '''
        return self+b
            
    def __sub__(self, b):
        '''
        Realiza la resta entre matrices y matrices con números.
        
        Condición:
        ---------
        Las dos matrices ingresadas deben ser del mismo tamaño.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida = [n-b for n in selfm.elems]
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[selfm.elems[m]-b.elems[m] for m in range(0, len(b.elems))]
            else:
                print('No se pueden restar dos matrices de distinto tamaño')
        else:
            print(f'No se puede restar {type(self)} con {type(b)}.')
            
        return myarray1(salida, self.r, self.c, selfm.by_row)
    
    def __rsub__(self,b):
        '''
        Realiza la resta entre matrices y números leyendo el primer argumento 
        como un numero real.

        '''
        return self*(-1) + b
    
    def __mul__(self, b):
        '''
        Realiza el producto entre matrices y matrices con números.
        
        Condición:
        ---------
        Las dos matrices ingresadas deben ser del mismo tamaño.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida = [n*b for n in selfm.elems]
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[selfm.elems[m]*b.elems[m] for m in range(0, len(b.elems))]
            else:
                print('No se pueden multiplicar dos matrices de distinto tamaño')
        else:
            print(f'No se puede multiplicar {type(self)} con {type(b)}.')
            
        return myarray1(salida, selfm.r, selfm.c, selfm.by_row)
    
    def __rmul__(self,b):
        '''
        Realiza el próducto entre matrices y números leyendo el primer argumento 
        como un numero real.

        '''
        return self * b
    
    def __pow__(self,b):
        '''
        Realiza la potencia de una matriz.
        
        Condición
        ---------
        La matriz debe ser elevada unicamente por un escalar.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
        if isinstance(b, int):
            salida = [n**b for n in selfm.elems]
            
        else:
            print(f'No se puede realizar la potenciación entre un {type(self)} con {type(b)}.')
            
        return myarray1(salida, selfm.r, selfm.c, selfm.by_row)
    
    def __matmul__(self,b):
        '''
        Realiza la multiplicación entre dos matrices.
        
        Condición
        ---------
        La primer matriz tenga las mismas filas que columnas de 
        las segunda
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------
            
        if isinstance(c, type(self)):
            

            if self.c == b.r:
                salida =[] 
                col= 1
                row= 1
                for i in range(1, selfm.r*b.c+1):
                    
                    salida.append(sum((selfm.get_row(row)*b.get_col(col)).elems))
                    col+=1
                    
                    if col == b.c+1:
                        row+=1
                        col+=1-col
                        
                return myarray1(salida, selfm.r, b.c, selfm.by_row)
            
        else:
            print('Solo se puede aplicar multiplicación matrcial entre matrices')
            
    def right_prod(self,matriz):
        '''
        Multiplica el objeto en el que se llama la función por la matriz ingresada
        a la derecha.

        Parameters
        ----------
        matriz : myarray1
            Matriz por el que se quiere multiplicar el objeto.
            
        '''
        return self@matriz
    
    def left_prod(self, matriz):
        '''
        Multiplica el objeto en el que se llama la función por la matriz ingresada
        a la izquierda.

        Parameters
        ----------
        matriz : myarray1
            Matriz por el que se quiere multiplicar el objeto.
            
        '''
        return matriz@self
    
    def identity(self,n):
        '''
        Subclase que genera una matriz cuadrada identidad a partir del número n
        ingresado.

        Parameters
        ----------
        n : int
            Define el tamaño de la matriz cuadrada.
            
        '''
        
        zeros=[0]*n*n
        
        for i in range(0,n*n, n+1 ):
            zeros[i]+=1 
            
        return myarray1(zeros,n,n, True)
        
                
    def eye_swap(self, j, k, n):
        '''
        Cambia los filas de la matriz identidad de acuerdo al cambio de la matriz
        original que se pide tanto por filas como por columnas.(es utilizada dentro
        de eswap cols y rows.)
        
        Condición
        --------
        Las filas o columnas a intercambiar deben existir.

        Parameters
        ----------
        j : int
            Fila que se quiere intercambiar por k.
        k : int
            Fila que se quiere intercambiar por j.
        n : int
            Tamaño de la matriz identidad.
        '''
        identidad=self.identity(n)
        eyelist=identidad.elems
        for i in (j,k):
            pos=identidad.get_pos(i,i)
            eyelist[pos]=0
        
        eyelist[identidad.get_pos(j,k)]=1
        eyelist[identidad.get_pos(k,j)]=1
            
        return eyelist
        
    def eswap_rows(self,j,k):
        '''
        Intercambia la fila j por la k a través de operadores de multiplicación.
        
        Condición:
        ---------
        Las filas deben existir dentro de la matriz orginal

        Parameters
        ----------
        j : int
            Fila a intercambiar por k.
        k : int
            Fila a intercambiar por j.
            
        '''
        if j in range(1,self.r+1) and k in range(1,self.r+1):
            
            return myarray1(self.eye_swap(j, k, self.r), self.r,self.r, True)@self
        else:
            print(f'Error: Los números ingresados estan fuera del rango de filas (1,{self.r}).')
    
    def eswap_cols(self,l,m):
        '''
        Intercambia la columna l por la m a través de operadores de multiplicación.
        
        Condición:
        ---------
        Las columnas deben existir dentro de la matriz orginal

        Parameters
        ----------
        l : int
            Columna a intercambiar por m.
        m : int
            Columna a intercambiar por l.
            
        '''
        if l in range(1,self.c+1) and m in range(1,self.c+1):
            
            return self@myarray1(self.eye_swap(l, m, self.c), self.c,self.c, True)
        
        else:
            print(f'Error: Los números ingresados estan fuera del rango de columnas (1,{self.c}).')
            
    def edel_row(self,e):
        '''
        Se encarga de eliminar la fila "e" ingresada a través de operadores de multiplicación.
        
        Condición
        ---------
        La fila ingresada debe existir dentro de la matriz original.
        
        Parameters
        ----------
        e : int
            Fila que se quiere eliminar.

        '''
        if e in range(1,self.r+1):
            
            identidad=self.identity(self.r).elems
            
            [identidad.pop((e-1)*self.r) for i in range(0, self.r)]
            
            return myarray1(identidad, self.r-1, self.r, True)@self
        
        else:
            
            print(f'Error: Los números ingresados estan fuera del rango de filas (1,{self.r}).')
    
    def edel_col(self,e):
        '''
        Se encarga de eliminar la columna "e" ingresada a través de operadores de multiplicación.
        
        Condición
        ---------
        La columna ingresada debe existir dentro de la matriz original.
        
        Parameters
        ----------
        e : int
            Columna que se quiere eliminar.

        '''
        if e in range(1,self.c+1):
            
            eye=self.identity(self.c).elems
            identidad=eye.copy()#TENER CUIDADO<-------------------------------------
    
            [identidad.pop(e-1+i) for i in range(0,len(eye)-self.c, self.c-1)]
            
            return self@myarray1(identidad, self.c, self.c-1, True)
        
        else:
            
            print(f'Error: Los números ingresados estan fuera del rango de columnas (1,{self.c}).')
    
    def adjunta(self):
        '''
        Saca la matriz inversa de la matriz original.
        '''
        matriz=self.traspose()
        
        determinante=self.det()
        if determinante != 0:
            adj=[matriz.edel_row(matriz.get_coords(i)[0]).edel_col(matriz.get_coords(i)[1]).det()*((-1)**(i+1)) for i in range(0,len(matriz.elems))]
            
            return myarray1(adj, self.r, self.c, self.by_row)*(1/determinante)
        else:
            print('Error: No se puede calcular la inversa de esta matriz dado que su determinnte es igual a cero.')


    def my_print(self):
        
        for k in range(1,self.r+1):
            
            print(self.get_row(k).elems)
            
        print('\n')
#%%
if __name__ == '__main__':
    
    
    a=myarray1([2,4,0,2,0,
                3,0,5,1,0,
                0,6,2,0,3,
                4,0,2,0,4,
                0,6,1,0,2],5, 5, True)
    
    b=myarray1([3,-1,2
                ,1,2,1
                ,0,4,0],3, 3, True)
    
    c=myarray1([1,2,
                3,4,
                5,6],3, 2, True)

    d=myarray1([1,2,3,
               4,5,6,
               7,8,9],3,3,True)
    
    
    
    
    print('d.get_pos(2,2):', d.get_pos(2, 2),'\n')
    
    print('d.get_coords(2):', d.get_coords(2),'\n')
    
    print('d.switch()\n-----------')
    d.switch().my_print()
    
    print('d.get_row(2)\n-----------')
    d.get_row(2).my_print()
    
    print('d.get_col(3)\n-----------')
    d.get_col(3).my_print()
    
    print('d.get_elem(2,1):',d.get_elem(2,1),'\n-----------\n')
    
    print('d.del_row(2)\n-----------')
    d.del_row(2).my_print()
    
    print('d.del_col(3)\n-----------')
    d.del_col(3).my_print()
    
    print('d.swap_rows(1,3)\n-----------')
    d.swap_rows(1,3).my_print()
    
    print('d.swap_cols(1,2)\n-----------')
    d.swap_cols(1,2).my_print()
    
    print('d.scale_row(2,2)\n-----------')
    d.scale_row(2, 2).my_print()
    
    print('d.scale_cols(3,3)\n-----------')
    d.scale_cols(3,3).my_print()
    
    print('d.traspose()\n-----------')
    d.traspose().my_print()
    
    print('d.flip_rows()\n-----------')
    d.flip_rows().my_print()
    
    print('d.flip_cols()\n-----------')
    d.flip_cols().my_print()
    
    print('d.shift(2,abajo)\n-----------')
    d.shift(2, 'abajo').my_print()
    
    print('d.shift(2,arriba)\n-----------')
    d.shift(2, 'arriba').my_print()
    
    print('a.det():', a.det(), '\n-----------\n')
    
    print('d+b(radd)\n-----------')
    (d+b).my_print()
    
    print('2+d(radd)\n-----------')
    (2+d).my_print()
    
    print('d-b (sub)\n-----------')
    (d-b).my_print()
    
    print('2-d(rsub)\n-----------')
    (2-d).my_print()
    
    print('2*d(rmul)\n-----------')
    (2*d).my_print()
    
    print('b*d (mul)\n-----------')
    (b*d).my_print()
    
    print('d**2(__pow__)\n----------')
    (d**2).my_print()
    
    print('b@c(__matmul__)\n-----------')
    (b@c).my_print()
    
    print('b.right_prod(d)\n------------')
    b.right_prod(d).my_print()
    
    print('b.left_prod(d)\n------------')
    b.left_prod(d).my_print()
    
    print('b.identity(d)\n------------')
    b.identity(3).my_print()
    
    print('b.eswap_rows(1, 3)\n------------')
    b.eswap_rows(1, 3).my_print()
    
    print('b.edel_row(1)\n-----------')
    b.edel_row(1).my_print()
    
    print('b.edel_col(2)\n-----------')
    b.edel_col(2).my_print()
    
    print('b.adjunta()\n------------')
    b.adjunta().my_print()
    
    
    
    
    
    
    
    
    
    



            
            
            