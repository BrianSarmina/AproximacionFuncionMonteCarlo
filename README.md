# AproximacionFuncionMonteCarlo
Aproximación de la funcion exp(-x^2) usando el Metodo Monte Carlo

Autores: (1) Ing. Brian Sarmina, (2) Ing. Jose Luis Barbosa Pacheco.
Correos: (1) brian.garsar.6@gmail.com, (2)...

Este programa se encarga de calcular la aproximación de una función, que en este caso es "exp(-x^2)", la aproximación de la función solo se plasma en el rango comprendido de 0 a 1, eso sin importar si la función comprende una escala mayor.

Este programa puede ser modificado para implementarse otro tipo de funciones, solo deben modificarse los renglones 43 a 48 donde se tienen las funciones descritas de manera explicita.

El programa despliega una ventana donde se solicita ingresar un numero "n" que corresponde al número de variables aleatorias que serán usadas para realizar la aproximación de la función, al final del programa se muestra la grafica generada, el número "n" y la función calculada.

Los paquetes necesarios para correr el código son:
 - import numpy as np
 - import math as m
 - import random as r
 - import matplotlib.pyplot as plt
 - import tkinter as tk
 - from tkinter.ttk import *

