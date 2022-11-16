#!/usr/bin/python3
# coding=utf-8
import sys

#Leemos cada línea de la entrada estándar
for line in sys.stdin:  
  #Dividimos en palabras cada línea
  words = line.split()  
  #Iteramos sobre cada palabra contenida en words
  for word in words:    
  	#Escribimos por salida estándar el par <Clave,Valor>
	#En este caso la Clave será la palabra en cuestión y el valor será 1
	print '%s\t%s' % (word,1)
