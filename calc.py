import tkinter as tk
from tkinter import messagebox, font

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('330x330')
        self.resizable(0,0)
        self.title('Calculadora')
        # self.iconbitmap('/calc/calculadora.ico')
        
        # Atributos de clase
        self.expresion = ''
        # Caja de texto(input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()
    
    # Metodos de Clase
    # Metodo para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=325, height = 50, bg='grey')        
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width = 24, 
                           justify=tk.RIGHT).grid(row=0, column=0, ipady=10)
        
        # Creamos otro frame para la parte de botones
        botones_frame = tk.Frame(self, width = 325, height= 330, bg=('grey'))
        botones_frame.pack()
        
        # Primer Renglon
        # Boton limpiar
        boton_limpiar = tk.Button(botones_frame, text='Clear', width = 34, height=3, bd=0, bg='#eee',
                                  cursor='hand2', command=self._evento_limpiar).grid(row=0,column=0,columnspan=3,
                                                                                     padx=1,pady=1)
        # Boton dividir
        boton_dividir = tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', 
                                  cursor='hand2', command=lambda: self._evento_click('/')).grid(
                                      row=0,column=3,padx=1,pady=1)
        
        # Segundo Renglon
        # Boton numero 7
        boton_siete = tk.Button(botones_frame, text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(7)).grid(row=1, column=0, padx=1, pady=1)
        # Boton numero 8
        boton_ocho = tk.Button(botones_frame, text='8', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(8)).grid(row=1, column=1, padx=1, pady=1)
        # Boton numero 9
        boton_nueve = tk.Button(botones_frame, text='9', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(9)).grid(row=1, column=2, padx=1, pady=1)
        # Boton simbolo multiplicacion
        boton_mult = tk.Button(botones_frame, text='x', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('*')).grid(row=1, column=3, padx=1, pady=1)
        
        # Tercer Renglon
        # Boton numero 4
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(4)).grid(row=2, column=0, padx=1, pady=1)
        # Boton numero 5
        boton_cinco = tk.Button(botones_frame, text='5', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(5)).grid(row=2, column=1, padx=1, pady=1)
        # Boton numero 6
        boton_seis = tk.Button(botones_frame, text='6', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(6)).grid(row=2, column=2, padx=1, pady=1)
        # Boton simbolo resta
        boton_resta = tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('-')).grid(row=2, column=3, padx=1, pady=1)
        
        # Cuarto Renglon
        # Boton numero 1
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(1)).grid(row=3, column=0, padx=1, pady=1)
        # Boton numero 2
        boton_dos = tk.Button(botones_frame, text='2', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(2)).grid(row=3, column=1, padx=1, pady=1)
        # Boton numero 3
        boton_tres = tk.Button(botones_frame, text='3', width=11, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click(3)).grid(row=3, column=2, padx=1, pady=1)
        # Boton simbolo suma
        boton_suma = tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('+')).grid(row=3, column=3, padx=1, pady=1)
        
        # Quitnto Renglon
        # Boton numero 0
        boton_0 = tk.Button(botones_frame, text='0', width=22, height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self._evento_click('0')).grid(row=4, column=0, columnspan=2, 
                                                                          padx=1, pady=1)
        # Boton punto
        boton_punto = tk.Button(botones_frame, text='.', width=11, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self._evento_click('.')).grid(row=4, column=2, padx=1, pady=1)
        # Boton simbolo igual
        boton_igual = tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2',
                            command=self._evento_evaluar).grid(row=4, column=3, padx=1, pady=1)
        
    def _evento_evaluar(self):
        # eal evalua la expresion str como una expresion aritmetcia
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''
        

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
        
    def _evento_click(self, elemento):
        # Concatenmos el numevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
        
if __name__ == '__main__':
    # for font in font.families():
    #     print(font)
    calculadora = Calculadora()
    calculadora.mainloop()