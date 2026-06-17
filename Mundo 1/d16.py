import math

#n = float(input('Digite um número: '))
#print('O número {} tem a parte inteira {:.0f}' .format(n, n)) #usando gambiarra e assim,
#agora usando math

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {:.0f}' .format(n, math.trunc(n)))
