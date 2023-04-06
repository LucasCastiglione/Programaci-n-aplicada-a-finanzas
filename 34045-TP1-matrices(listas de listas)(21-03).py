# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:43:50 2023

@author: casti
"""

class myarray2():
    '''
    Condiciones
    -----------
    Las matrices se van a indexar de forma matemática, es decir que tanto filas
    como columnas empiezan en el número 1.
    
    El número de filas x columna debe coincidir con el largo de la lista elems.
    '''
    def __init__(self, elems, r, c, by_row):
        
        largo=0
        for fila in elems:
            
            if type(fila) == int:
                largo+=1
            else:
                largo+=len(fila)
            
        if largo != r*c:
        #if len(elems)*len(elems[0]) != c*r:    
            
            print(f'Error: Las filas por columnas ({r*c}) no coincide \ncon el largo de la lista de listas({largo}).')
            
        else:
            self.elems=elems
            self.r=r
            self.c=c
            self.by_row=by_row
        
    
    
    def get_pos (self,j,k):
        '''
        Toma las coordenadas j,k en la matriz y devuelve la posicion m asociada 
        en la lista elems.
        
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
        if j <= self.r and k <= self.c:
            
            n=j*self.c-(self.c-k)-1#le resto uno porque las posiciones empiezan de cero
            
            return n
        
        else:
            print(f'Los números ingresados estan fuera de rango, reingrese numeros menor que {self.r} en la fila y menor que {self.c} en la columna.')
    
    def get_coords(self,n):
        '''
        Toma una posición m en la lista y devuelve en forma de tupla las 
        coordenadas j,k correspondientes en la matriz.
        
        Condición
        ---------
        La función esta realizada a partir del indexin de listas por lo que las 
        posiciones comienzan desde cero.
        
        Se deben ingresar posiciones como si fuese una lista continua y no una lista
        de listas
        Parameters
        ----------
        n : int
            Posición de la cual se buscan las coordenadas.
        '''
        if n in range(0, self.c*self.r):
            self.n=n
            a=0+self.n
            
            while a>0:
                
                a-=self.c
            
            if a < 0:
                a+=self.c
                
            k=a+1 #le resto al n (n+1, porque las posicion es uno menos) le resto el nro de columnas enteras y me queda k 
            
            j=int((self.n+self.c-k+1)/self.c) #viene de despejar j de la funcion get_pos
            
            return (j,k)
        
        else:
            print(f'Error: La posición pedida ({n}) esta fuera de rango.')
    
    def switch(self):
        '''
        Devuelve un objeto con la misma matriz, pero alterando la lista elems y 
        cambiando el valor de verdad de by_row.

        Returns
        -------
        Type: myarray1
        
        '''
        matriz=[]
        lista=[]
        contador = 0
        while contador != self.c:
            
            for fila in self.elems:
                
                lista.append(fila[contador])

            contador+=1
        
        f=0+self.c
        
        for i in range(0,self.r):
            matriz.append(lista[f-self.c:f])
            f+=self.c
            
        if self.by_row == False:
            
            by_who = True
            
        else:
            
            by_who = True
        
        return myarray2(matriz, self.r, self.c, by_who)
            
    
    def get_row(self, j):
        '''
        Devuelve la fila j.
        
        Condición
        ---------
        j debe estar entre el número de filas de la matriz.
        
        las filas se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        j : int
            Número de fila que se busca.
            
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------------------------------------
        if j in range(1,selfm.r+1):
            
            return selfm.elems[j-1]
        
        else:
            print(f'Errror: Solo puedes ingresar números entre 1 y {selfm.r}.')
            
    def get_col(self,k):
        '''
        Devuelve la columna k
        
        Condición
        ---------
        k debe estar entre el número de columnas de la matriz.
        
        las filas se deben llamar en órden matmático por lo que comienzan en 1.
        
        Parameters
        ----------
        k : int
            Número de columna que se busca.
            
        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------------------------------------- 
        columna=[]
        
        if k in range(1,selfm.c+1):
            
            for fila in selfm.elems:
                
                columna.append(fila[k-1])
                
            return columna
        else:
            print(f'Errror: Solo puedes ingresar números entre 1 y {selfm.c}.')
     
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
        #-------------------------------------
        
        if j <=len(selfm.elems) and k <= len(selfm.elems[0]) and j>0 and k >0:  
            return selfm.elems[j-1][k-1]
        else:
            print('Error: Los números ingresados estan fuera de rango')
        
    
        
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
        #----------------------------------------------------------------------
        if j in range(1,selfm.r+1):
            matrizcopy=[]
            
            for fila in self.elems:
                matrizcopy.append(fila.copy())
            matrizcopy.pop(j-1)
            
            return myarray2(matrizcopy, selfm.r-1, selfm.c, selfm.by_row)
        
        else:
            print(f'Error: Solo puedes eliminar filas entre 1 y {selfm.r}')
        
    def del_col(self, k):
        '''
        Devuelve un objeto de la clase habiendo eliminando la columna k.
        
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
        #------------------------------------------------------
        matrizcopy=[]
        
        for fila in self.elems:
            matrizcopy.append(fila.copy())
            
        if k in range(1, selfm.c+1):
            for fila in matrizcopy:
                
                fila.pop(k-1)
            
            return myarray2(matrizcopy, selfm.r, selfm.c-1, selfm.by_row)
        
        else:
            print(f'Error: Solo puedes eliminar filas entre 1 y {selfm.r}')
            
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
            
        if j in range(1,selfm.r+1) and k in range(1,selfm.r+1):
            listacopy=selfm.elems.copy()
            
            listacopy[j-1]=selfm.elems[k-1]
            listacopy[k-1]=selfm.elems[j-1]
            
            return myarray2(listacopy, selfm.r, selfm.c, selfm.by_row)
        
        else: 
            print(f'Error: Alguna de sus filas esta fuera del rango, entre 1 y {selfm.r}.')
        
        
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
        #-------------------------------------------------------------------
        if l in range(1,selfm.c+1) and m in range(1,selfm.c+1):
            
            return selfm.traspose().swap_rows(l,m).traspose()
        else:
            print(f'Error: Alguna de sus columnas esta fuera del rango, entre 1 y {selfm.c}.')
    
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
        #---------------------------------------------------------------
        if j in range(1, selfm.r+1):
            matriz=selfm.elems.copy()
            row=selfm.get_row(j)
            row_mul=[]
            
            for i in row:
                
                row_mul.append(i*x)
                
            matriz[j-1]=row_mul
            
            return myarray2(matriz,selfm.r, selfm.c, selfm.by_row)
        else:
            print(f'Error: La fila ingresada esta fuera del rango, entre 1 y {selfm.r}.')
    
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
        #---------------------------------------------------------------------
        if k in range(1, selfm.c+1):
            return selfm.traspose().scale_row(k,y).traspose()
        
        else:
            print(f'Error: La columna ingresada esta fuera del rango, entre 1 y {selfm.r}.')
    
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
        #----------------------------------------------------------------------

        lista=list(zip(*self.elems))
        matriz=[list(tupla) for tupla in lista]
        
        return myarray2(matriz, selfm.c, selfm.r, True)
    
    
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
        #----------------------------------------------------------
        lista=[]
        for fila in selfm.elems:
            
            lista.append(list(reversed(fila)))
        
        return myarray2(lista, selfm.r, selfm.c, selfm.by_row)
    
    def flip_cols(self):
        '''
        Devuelve las filas volteadas [[1],      [[3]
                                      [2],---->  [2]
                                      [3]]       [1]]   

        Returns
        -------
        myarray2
            Nuevo objeto dónde las columnas estan volteadas respecto al original.

        '''
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        #---------------------------------------------------------------
        return selfm.traspose().flip_rows().traspose()

    def shift (self, n, m):#n empieza de cero
        '''
        
        Devuelve una lista desplazar las filas cuantas veces se pida para arriba o para abajo.
        
        Condición
        ---------
        m debe decir explicitamente "arriba" o "abajo"
        
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
        if m == 'abajo':
            
            lis=[]
            for i in range(1,n+1):
               
                lis.append(selfm.elems[selfm.r-1-i])
             
            noesta=[]
            for fila in selfm.elems:
                
                if fila not in lis:
                    
                    noesta.append(fila)
            
            lista=noesta+lis

        elif m == 'arriba':
           
           lis=[]
           for i in range(0,n):
              
               lis.append(selfm.elems[i])
              
           noesta=[]
           
           
           for fila in selfm.elems:
               
               if fila not in lis:
                   
                   noesta.append(fila)
           
           lista=noesta+lis
           
        
        else:
            print('Error: Solo puede ir para "arriba" o "abajo".')
            
        return myarray2(lista, selfm.r, selfm.c, selfm.by_row)
    
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
        #---------------------------------------------------------------------
        if self.c == self.r:
            determinante=0
            
            if len(selfm.elems) == 1:
                
                determinante=selfm.elems[0][0]
                
                return determinante
            
            else:
                
                for i in range(1,selfm.c+1):
                    
                    submatriz=selfm.del_row(1).del_col(i)
                    coef=selfm.get_elem(1,i)
                    determinante+=((-1)**i)*coef*submatriz.det()
     
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
        #----------------------------------------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida=[]
            for i in range(0, selfm.r): 
                salida.append([n+b for n in selfm.elems[i]])
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[]
                for i in range(0, selfm.r):
                    salida.append([selfm.elems[i][m]+b.elems[i][m] for m in range(0, selfm.c)])
            else:
                print('No se pueden sumar dos matrices de distinto tamaño')
        else:
            print(f'No se puede sumar {type(self)} con {type(b)}.')
            
        return myarray2(salida, self.r, self.c, selfm.by_row)
    
    def __radd__(self,b):
        '''
        Realiza la suma entre matrices y números leyendo el primer argumento 
        como un numero real.

        '''
        return self + b
    
    def __sub__(self,b):
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
        #----------------------------------------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida=[]
            for i in range(0, selfm.r): 
                salida.append([n-b for n in selfm.elems[i]])
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[]
                for i in range(0, selfm.r):
                    salida.append([selfm.elems[i][m]-b.elems[i][m] for m in range(0, selfm.c)])
            else:
                print('No se pueden restar dos matrices de distinto tamaño')
        else:
            print(f'No se puede restar {type(self)} con {type(b)}.')
            
        return myarray2(salida, self.r, self.c, selfm.by_row)
    
    def __rsub__(self,b):
        '''
        Realiza la resta entre matrices y números leyendo el primer argumento 
        como un numero real.

        '''
        return self*(-1) + b
    
    def __mul__(self,b):
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
        #----------------------------------------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida=[]
            for i in range(0, selfm.r): 
                salida.append([n*b for n in selfm.elems[i]])
        elif isinstance(b, type(selfm)):
            if len(b.elems) == len(selfm.elems):
                salida=[]
                for i in range(0, selfm.r):
                    salida.append([selfm.elems[i][m]*b.elems[i][m] for m in range(0, selfm.c)])
            else:
                print('No se pueden multiplicar dos matrices de distinto tamaño')
        else:
            print(f'No se puede multiplicar {type(self)} con {type(b)}.')
            
        return myarray2(salida, self.r, self.c, selfm.by_row)
    
    def __rmul__(self,b):
        '''
        Realiza el producto entre matrices y números leyendo el primer argumento 
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
        #----------------------------------------------------------------------
        if isinstance(b, int) or isinstance(b, float):
            salida=[]
            for i in range(0, selfm.r): 
                salida.append([n**b for n in selfm.elems[i]])   
        else:
            print(f'No se puede realizar la potenciación entre un {type(self)} con {type(b)}.')
            
        return myarray2(salida, selfm.r, selfm.c, selfm.by_row)
    
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
        #----------------------------------------------------------------------
        if isinstance(b, type(self)):
            

            if selfm.c == b.r:
                
                filas=[]
                [filas.extend([selfm.get_row(ind)]*b.c) for ind in range(1, selfm.r+1)]
                cols=b.traspose().elems*selfm.r
                m=list(map(lambda tupla: sum(list(map(lambda x: x[0]*x[1],list(zip(*tupla))))),list(zip(filas,cols))))
                matriz, inicio, fin=[], 0, b.c
                for i in range(0, selfm.r):
                    
                    matriz.append(m[inicio:fin])
                    inicio+=b.c
                    fin+=b.c
                    
                return myarray2(matriz, selfm.r, b.c, selfm.by_row)
            
            else:
                print('El número de filas y columnas no coincide')
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
        
        zeros=[]
        for i in range(1,n+1):
            
            zrow=[0,]*n
            zrow[i-1]+=1
            zeros.append(zrow)
            
        return myarray2(zeros,n,n,True)
    
    def eye_swap(self, j, k, n):
        '''
        Cambia los filas de la matriz identidad de acuerdo al cambio de la matriz
        original que se pide tanto por filas como por columnas.
        
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
        for i in (j-1,k-1):
            identidad.elems[i][i]=0
        
        identidad.elems[j-1][k-1]=1
        identidad.elems[k-1][j-1]=1
         
        return identidad.elems
        
    def eswap_rows(self,j,k):
        '''
        Intercambia la fila j por la k.
        
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
            
            return myarray2(self.eye_swap(j, k, self.r), self.r,self.r, True)@self
        else:
            print(f'Error: Los números ingresados estan fuera del rango de filas (1,{self.r}).')
    
    def eswap_cols(self,l,m):
        '''
        Intercambia la columna l por la m.
        
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
            
            return self@myarray2(self.eye_swap(l, m, self.c), self.c,self.c, True)
        
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
            identidad=self.identity(self.r)
            identidad.elems.pop(e-1)
            
            return myarray2(identidad.elems, self.r-1, self.r, True)@self
        
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
            
            identidad=self.identity(self.c).elems
            
            [identidad[i].pop(e-1) for i in range(0, len(identidad))]
            
            return self@myarray2(identidad, self.c, self.c-1, True)
        
        else:
            
            print(f'Error: Los números ingresados estan fuera del rango de columnas (1,{self.c}).')
            
        
    def adjunta(self):
        '''
        Saca la matriz inversa de la matriz original.
        '''
        matriz=self.traspose()
        determinante=self.det()
        if determinante != 0:

            listadj=[matriz.edel_row(matriz.get_coords(i)[0]).edel_col(matriz.get_coords(i)[1]).det()*((-1)**(i+1)) for i in range(0,self.c*self.r)]
            adj=[listadj[i:i+self.c] for i in range(0, self.c*self.r, self.c)]
            
            return myarray2(adj, self.r, self.c, self.by_row)*(1/determinante)
        else:
            print('Error: No se puede calcular la inversa de esta matriz dado que su determinnte es igual a cero.')
            
    def my_print(self):
        
        
        if self.by_row == False:
            
            selfm=self.switch()
            
        else: 
            selfm=self
        
        for fila in selfm.elems:
            
            print(fila)
            
        print('\n')
#%%
if __name__ == '__main__':
    
    a=myarray2([[2,4,0,2,0],
                [3,0,5,1,0],
                [0,6,2,0,3],
                [4,0,2,0,4],
                [0,6,1,0,2]],5, 5, True)
    
    b=myarray2([[3,-1,2]
                ,[1,2,1]
                ,[0,4,0]],3, 3, True)
    
    c=myarray2([[1,2],
                [3,4],
                [5,6]],3, 2, True)

    d=myarray2([[1,2,3],
                [4,5,6],
                [7,8,9]],3,3,True)
    
    
    print('d.get_pos(2,2):', d.get_pos(2, 2),'\n')
    
    print('d.get_coords(2):', d.get_coords(2),'\n')
    
    print('d.switch()\n-----------')
    d.switch().my_print()
    
    print('d.get_row(2)\n-----------')
    print(d.get_row(2),'\n')
    
    print('d.get_col(3)\n-----------')
    print(d.get_col(3),'\n')
    
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