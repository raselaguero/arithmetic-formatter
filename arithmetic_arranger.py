def arithmetic_arranger(lista, boolean=False):
    operan1, operan2, line, result = [], [], [], []
    if len(lista) <= 5:
        for l in lista:
            if not l.__contains__('+') and not l.__contains__('-'):
                 print("Error: Operator must be '+' or '-'.")
                 break
            elif l.__contains__('+'):
                item = l.partition('+')
            elif l.__contains__('-'):
                item = l.partition('-')
            val1 = item[0].strip()
            oper = item[1]
            val2 = item[2].strip()
            if val1.isdigit() is True and val2.isdigit() is True:
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
                else:
                    print('Error: Numbers cannot be more than four digits.')
            else:
                print("Error: Numbers must only contain digits.")
        print('    '.join(operan1))
        print('    '.join(operan2))
        print('    '.join(line))
        print('    '.join(result))
    else:
        print("Error: Too many problems.")


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)