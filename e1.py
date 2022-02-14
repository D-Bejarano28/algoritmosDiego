"""
## Pregunta 1

### 1.A (4 ptos)

Dada una oración, escriba una función en Python para verificar si esa oración es un Pangrama o no.

> Un pangrama es una oración que contiene todas las letras del alfabeto inglés

### 1.B (4 ptos)

Realice una función que además determine cuántas letras se repiten en la oración original

**Ejemplo de Input:**

```python
pangrama('El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo')
```

**Output:**

```shell
Si es un Pangrama
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Las letras del output deben ser de la oración del pangrama
```
"""

def panagrama(alfabet,sentence):
  cont_f = 0
  
  sentence = sentence.lower()
  for i in alfabet:
    if i not in sentence:
      cont_f += 1
  if cont_f >= 1:
    print('La horacion ingresada no es un panagrama!!')
    return False
  else:
    print('la horacion ingresada es un panagrama!!')


def repetidas(sentence,lista):

  for i in sentence:
    if sentence.count(i) > 1:
      if (not i in lista):
        lista.append(i)
  
  for i in lista:
     if i == ',' or i == ' ':
       lista.remove(i)
  return lista



def main():

  sentence = input('Ingrese una oración: ')
  while (sentence.isalnum()):
    sentence = input('Ingrese un dato válido: ')

  #Lista para guardar los caracteres repetidos  
  lista = []

  alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  panagrama(alfabet,sentence)

  print(repetidas(sentence,lista))


main()
  
