#!/usr/bin/python3
# coding=utf-8
import sys
	
curr_word = None
curr_count = 0
	
# Procesamos cada Clave-Valor que produce la función map
for line in sys.stdin:
	
  #Dividimos la clave y el valor
  word, count = line.split('\t')
	
  #Convertimos a entero el valor
  count = int(count)

  #Si la palabra actual es la misma que la previa, incrementamos el contador
  #en otro caso imprimimos la palabra en cuestión con el contador
  if word == curr_word:
    curr_count += count
  else:
    if curr_word:   
      print '%s\t%s' % (curr_word, curr_count)
			
    #Actualizamos las variables a la nueva palabra
    curr_word = word
    curr_count = count
	
#Imprimimos la última palabra
if curr_word == word:
  print '%s\t%s' % (curr_word, curr_count)
