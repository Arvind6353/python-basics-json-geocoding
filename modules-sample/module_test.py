#import module1.isPrime as isp
from module1 import isPrime as isp
import module1.module2.isPrime1 as isp1

print('methods inside module1.isprime ------',dir(isp))

print('methods inside module1.module2.isprime1 ------',dir(isp1))

print(' is 21 a prime no -',isp.checkForPrime(21))

print(' is 2 a prime no -',isp1.checkForPrime1(2))