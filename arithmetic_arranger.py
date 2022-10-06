def arithmetic_arranger(lista, boolean=False):
    operan1, operan2, line, result, space = [], [], [], [], '    '
    if len(lista) <= 5:
        letter = ' '.join(lista)
        mas, menos = letter.count('+'), letter.count('-')
        mas += menos
        if mas == len(lista):
            mas = letter.replace(' + ', '')
            menos = mas.replace(' - ', '')
            mas = menos.replace(' ', '')
            if mas.isdigit() is True:
                compren = [True for i in menos.split() if len(i) > 8]
                if len(compren) == 0:
                    for l in lista:
                        if l.__contains__('+'):
                            item = l.partition('+')
                        if l.__contains__('-'):
                            item = l.partition('-')
                        val1 = item[0].strip()
                        oper = item[1]
                        val2 = item[2].strip()
                        if len(val1) <= 4 and len(val2) <= 4:
                            linea = max(len(val1), len(val2)) + 2
                            just1 = linea - len(val1)
                            just2 = linea - (len(val2) + 2)
                            if boolean is False:
                                operan1.append(val1.rjust(len(val1)+just1))
                                operan2.append(oper + ' ' + val2.rjust(len(val2)+just2))
                                line.append('-'*linea)
                            else:
                                if oper == '+':
                                    calc = int(val1)+int(val2)
                                else:
                                    calc = int(val1)-int(val2)
                                just3 = linea - len(str(calc))
                                operan1.append(val1.rjust(len(val1)+just1))
                                operan2.append(oper + ' ' + val2.rjust(len(val2)+just2))
                                line.append('-'*linea)
                                result.append(str(calc).rjust(len(str(calc))+just3))
                    print(space.join(operan1), space.join(operan2), space.join(line), space.join(result), sep='\n')
                else:
                    print('Error: Numbers cannot be more than four digits.')
            else:
                print("Error: Numbers must only contain digits.")
        else:
            print("Error: Operator must be '+' or '-'.")
    else:
        print("Error: Too many problems.")


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)