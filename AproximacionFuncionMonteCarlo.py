#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:44:26 2020

Autores: (1) Ing. Brian Sarmina, (2) Ing. Jose Luis Barbosa Pacheco.
Correos: (1) brian.garsar.6@gmail.com, (2)..

@authors: bgs/jlb
"""

import numpy as np
import math as m
import random as r
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.ttk import *


# Función para calcular la "exp_montecarlo".
def exp_montecarlo(n_muestra):

    # Vectores para almacenar los datos de X (x_vals) y Y (y_vals = g(x)).
    x_vals = []
    y_vals = []

    x_graf_vals = []
    y_graf_vals = []

    # Generamos un "for loop" en función del número de muestra.
    for i in range(n_muestra):

        # Usamos la funcion r.random() para generar un valor pseudo-aleatorio
        # entre 0 y 1.
        x_val = r.random()

        # Calculamos valores para la gráfica de -5 a 5 para observar la coincidencia
        # de nuestro cálculo de 0 a 1.
        x_graf_val = r.uniform(-5.0, 5.0)
        x_graf_vals.append(x_graf_val)
        
        # Agregamos el valor de x a la lista "x_vals".
        x_vals.append(x_val)
        # Con el valor de x, evaluamos la función para ese punto y almacenamos
        # el valor obtenido
        y_val = m.exp((-1)*m.pow(x_val, 2))
        y_vals.append(y_val)

        # Valores para g(x) de gráfica "completa" de -5 a 5.
        y_graf_val = m.exp((-1)*m.pow(x_graf_val, 2))
        y_graf_vals.append(y_graf_val)

    # Transformamos las listas en "arreglos numpy", ya que "numpy" cuenta con
    # algoritmos de optimización que permiten operar datos en vectores de manera
    # más eficientes y rapidas.
    x_vals = np.array(x_vals)
    y_vals = np.array(y_vals)

    # Calculamos el valor de "theta_gorro" que es el valor de la integral
    # definida entre 0 y 1.
    theta_gorro = np.sum(y_vals) / n_muestra

    # Regresamos los valores de "x", "y" y "theta_gorro".
    return x_vals, y_vals, theta_gorro, x_graf_vals, y_graf_vals  

# Función que valida la entrada, dada por el usuario
def valida_entrada(event):
    n_valor = int(respuesta.get())
    respuesta.delete(0, tk.END)
    valor_resultado["text"] = n_valor
    
    # Llamamos a la función "exp_montecarlo que se encarga de calcular la integral
    # entre 0 y 1 "exp(-x^2)" y nos regresa los elementos generados para x, que son una
    # serie de valores pseudo-aleatorios entre 0 y 1 con su tamaño en funcion al tamaño
    # de muestra ingreado; recibimos los valores de la funcion "g(x)" para los valores
    # x generados y por ultimo obtenemos el theta gorro (el valor de la integral definida
    # en ese rango.
    valores_x, valores_y, theta_gorro, grafica_com_x, grafica_com_y = exp_montecarlo(n_valor)
    
    #Despliega textos de acuerdo a  la selección
    secret_number = respuesta.get()
    
    if secret_number.isnumeric :
        texto_resultado["text"] = "tamaño de la muestra introducido: "
        texto_integral["text"] = "Valor de la integral exp(-x^2) evaluada entre 0 y 1: "
        valor_integral["text"]= theta_gorro
    
        # Graficamos los datos obtenidos de x y g(x) (valores_y), donde primero graficamos la
        # "completa" (-10 a 10) y después los elementos obtenidos en el rango 0 a 1.
        plt.scatter(grafica_com_x, grafica_com_y,color='g')
        plt.scatter(valores_x, valores_y,color='r')
        plt.title('Gráfica entrada vs salida') 
        plt.xlabel("Valores X pseudo-aleatorios (entre 0 y 1)")
        plt.ylabel("Valores de g(x) para función exponencial")

        plt.show()
   
        
if __name__ == '__main__':
    #crea una ventana de diálogo para la entrada y salida de datos
    app = tk.Tk()
    app.title("Prog_1_equipo3")
    app.geometry('500x300')
    app.configure(bg='lightgray')
    
    title = tk.Label(app, text="Programas Análisis de Algoritmos", font=("", 16)).grid(row=0, columnspan=2, pady=10) 
    lbl_reponse = tk.Label(app, text="Valor de n : ", font=("", 12)).grid(row=1, column=0, pady=5, padx=5)
     
    respuesta = tk.Entry(app)
    respuesta.grid(row=1, column=1, pady=5, padx=5)
    respuesta.bind("<Return>", valida_entrada)
    
    texto_resultado = tk.Label(app, text="")
    texto_resultado.grid(row=2, column=0, pady=5, padx=5) 
    
    valor_resultado = tk.Label(app, text="")
    valor_resultado.grid(row=2, column=1, pady=5, padx=5)
    
    texto_integral = tk.Label(app, text="")
    texto_integral.grid(row=3, column=0, pady=5, padx=5)
    
    valor_integral = tk.Label(app, text="")
    valor_integral.grid(row=3, column=1, pady=5, padx=5)
    
    # Crea un boton para salir del programa y destruir la ventana
    boton = Button(app, text="Quit", command=app.destroy)
    boton.grid(row=10, column=1, pady=5, padx=5)
    
    app.mainloop()
