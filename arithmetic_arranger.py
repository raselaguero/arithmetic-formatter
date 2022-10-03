# Los estudiantes de primaria suelen colocar los problemas aritméticos en vertical para facilitar su resolución. Por ejemplo, "235 + 52" se convierte a:
#
#   235
# +  52
# -----
# Crea una función que reciba una lista de cadenas que sean problemas aritméticos y devuelva los problemas ordenados verticalmente y uno al lado del otro. La función debe tomar opcionalmente un segundo argumento. Cuando el segundo argumento se establezca como True, se deberán mostrar las respuestas.
#
# Ejemplo
# Llamando a la función:
#
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# Resultado:
#
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
# Llamando a la función:
#
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# Resultado:
#
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# Reglas
# La función devolverá la conversión correcta si los problemas suministrados están correctamente formateados, de lo contrario, devolverá una cadena que describe un error significativo para el usuario.
#
# Situaciones que devolverán un error:
# todo: Si hay demasiados problemas suministrados a la función. El límite es cinco, cualquier cosa más regresará: Error: Too many problems.
# todo: Los operadores apropiados que la función aceptará son suma y resta. La multiplicación y la división devolverán un error. Otros operadores que no se mencionan en este punto no tendrán que ser probados. El error devuelto será: Error: Operator must be '+' or '-'.
# todo: Cada número (operando) debe contener solo dígitos. De lo contrario, la función devolverá: Error: Numbers must only contain digits.
# todo: Cada operando (también conocido como número en cada lado del operador) tiene un máximo de cuatro dígitos de ancho. De lo contrario, la cadena de error devuelta será: Error: Numbers cannot be more than four digits.

# Si el usuario proporcionó el formato correcto de los problemas, la conversión que devuelva seguirá estas reglas:
# todo: Debe haber un solo espacio entre el operador y el más largo de los dos operandos, el operador estará en la misma línea que el segundo operando, ambos operandos estarán en el mismo orden proporcionado (el primero será el superior y el segundo el inferior).
# todo: Los números deben estar alineados a la derecha.
# Debe haber cuatro espacios entre cada problema.
# todo: Debe haber guiones en la parte inferior de cada problema. Los guiones deben recorrer toda la longitud de cada problema individualmente. (El ejemplo anterior muestra el aspecto que debe tener.)
# Desarrollo
# Escribe tu código en arithmetic_arranger.py. Durante el desarrollo de tu programa puedes utilizar main.py para probar el funcionamiento de tu función arithmetic_arranger(). Haz clic en el botón "run" y se ejecutará main.py.
#
# Pruebas
# Las pruebas unitarias para este proyecto están en test_module.py. Ejecutamos las pruebas de test_module.py a main.py para tu conveniencia. Las pruebas se ejecutarán automáticamente cada vez que pulses el botón "run". También puedes ejecutar las pruebas introduciendo pytest en la consola.
#
# Envío
# Copia el enlace de tu proyecto y envíalo a freeCodeCamp.

def arithmetic_arranger(lista, boolean=False):
    first, last, oper_list = [], [], []
    if len(lista) <= 5:
        for l in lista:
            if not l.__contains__('+') and not l.__contains__('-'):
                 print("Error: Operator must be '+' or '-'.")
                 break  # or continue
            elif l.__contains__('+'):
                item = l.partition('+')
            elif l.__contains__('-'):
                item = l.partition('-')
            val1 = (item[0]).strip()
            oper = item[1]
            val2 = (item[2]).strip()
            if val1.isdigit() is True and val2.isdigit() is True:
                if len(val1) <= 4 and len(val2) <= 4:
                    first.append(val1)
                    oper_list.append(oper)
                    last.append(val2)
                else:
                    print('Error: Numbers cannot be more than four digits.')
                    break
            else:
                print("Error: Numbers must only contain digits.")
                break
        show_result(first,oper_list,last, boolean)
    else:
        print("Error: Too many problems.")


def show_result(first,oper_list,last, boolean):
    for a,b,c in zip(first,oper_list,last):
        linea = max(len(a), len(c)) + 2
        just1 = linea - len(a)
        just2 = linea - (len(c) + 2)
        if boolean is False:
            print(a.rjust(len(a)+just1) + '\n' + b + ' ' + c.rjust(len(c)+just2) + '\n' + '-'*linea)
            # print(a, end=' ')
        else:
            if b == '+':
                calc = int(a)+int(c)
            else:
                calc = int(a)-int(c)
            just3 = linea - len(str(calc))
            print(a.rjust(len(a)+just1) + '\n' + b + ' ' + c.rjust(len(c)+just2) + '\n' + '-'*linea + '\n' + str(calc).rjust(len(str(calc))+just3))

arithmetic_arranger(['100 - 1', '2 + 1200', '3 + 3', '40 + 1', '500 - 1500'], True)