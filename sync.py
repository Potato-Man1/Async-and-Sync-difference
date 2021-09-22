import time
#The sleep is just copying an action that takes some time to finish
def foo():
    for i in range(10):
        time.sleep(1)
        print(1)

def fee():
    print('start task 1')
    time.sleep(5)
    print('done task 1!')
    
def fees():
    print('start task 2')
    time.sleep(4)
    print('done task 2!')
    

def main():
    fee()
    foo()
    fees()

main()
