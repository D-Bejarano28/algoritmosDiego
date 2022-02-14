"""
## Pregunta 2

La empresa de transporte Expresos Saman, ofrece tres destinos diarios a ciudades del país, en vehículos de capacidad de hasta 10 pasajeros. Para cada destino hay 3 vehículos. Estos destinos han sido clasificados de la siguiente forma:

| Codigo |    Destino     | Precio por Pasajero |
| :----: | :------------: | :-----------------: |
|   V    |    Valencia    |         500         |
|   P    | Puerto la Cruz |         700         |
|   B    |  Barquisimeto  |         800         |

Un cliente puede adquirir un pasaje para 1 o más personas hasta un máximo de 10, por lo que se debe validar que exista disponibilidad hacia el destino solicitado.

Al momento de la compra del pasaje, se le solicita al cliente los siguientes datos:

- Cédula de Identidad,
- Número de pasajeros,
- Ciudad destino.

Cuando el cliente solicita pasajes para más de 4 personas, se le otorga un descuento de 20% sobre el monto total a pagar.

Para cada cliente, el programa deberá desplegar la información del recibo con los siguientes datos:

- El número de cédula de identidad del cliente
- Cantidad de pasajeros
- Código y nombre del destino solicitado
- Monto bruto a pagar
- Monto de descuento (si no aplica, el programa mostrará cero)
- Monto del impuesto a pagar (IVA 16% del monto bruto menos el descuento)
- Monto neto a pagar

Al final del día el programa deberá calcular:

- La cantidad de clientes por destino (no pasajeros)
- El Monto Total Neto Facturado por destino
- El Monto Total de Descuentos otorgados por destino
- El Monto Total Neto Facturado por Expresos Saman
- Los datos del cliente que más dinero pagó

**Nota 1**: Al momento de la entrada de datos, el programa deberá validar si hay aún disponibilidad hacia el destino solicitado. Si no la hay deberá indicar un mensaje indicando que no hay disponibilidad hacia el destino solicitado, mostrando adicionalmente cuantos cupos quedan.

**Nota 2**: Si se venden los pasajes para todos los destinos y ya no hay más cupos, el programa deberá emitir un mensaje de que ya no hay cupos disponibles para ningún destino, dando el reporte del final del día y terminando la ejecución del programa.
"""

def compra(destinos,lista_pasajeros):
  ci = input('Ingrese su cedula de identidad: ')
  while (not ci.isnumeric()):
    ci = input('Ingrese su cédula correctamente: ')

  pasajeros = input('Ingrese el numero de pasajeros: ')
  while (not pasajeros.isnumeric()) or (int(pasajeros) not in range(1,31)):
    pasajeros = input('Ingrese una cantidad válida: ')
  
  pasajeros = int(pasajeros)

  destino = input('''
  Ingrese el destino de su preferencia:

  Valencia (V)
  Puerto La Cruz (P)
  Barquisimeto (V)

  ''')
  while destino != 'V' or destino != 'P' or destino != 'B':
    destino = input('Ingrese un dato válido: ')


  for i in destinos:
    if i['codigo'] == destino:
      precio = i['precio']

  monto_bruto = precio*pasajeros

  if pasajeros > 4:
    descuento = monto_bruto * 0.2
  else:
    descuento = 0

  






  

  



  
def main():

  destinos = [{'destino': 'valencia','codigo':'V','precio':500,'capacidad':30},
  {'destino': 'puerto la cruz','codigo':'P','precio':700,'capacidad':30},
  {'destino': 'barquisimeto','codigo':'B','precio':800,'capacidad':30}]

  while True:
    print('--BIENVENIDOS A EXPRESOS SAMÁN--\n')
    option = input('''
    Ingrese el numerode opcion que desea: 

    1. Comprar ticket
    2. Consultar estadisticas
    3. Salir

    ''')

    while (not option.isnumeric()) or (int(option) not in range(1,4)):
      option = input('Ingrese una opción válida: ')

    if option == '1':
      pass

    elif option == '2':
      pass

    else: 
      break

  pass
