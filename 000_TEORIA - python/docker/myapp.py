import time
import sys

a:int = 1

while a>0:
    sys.stdout.flush()
    print ("stampa infinta numero ", a)
    a+=1
    time.sleep(2)
        