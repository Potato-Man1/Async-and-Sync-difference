import time
#The sleep is just copying an action that takes some time to finish
#This part of the file is not needed for any explanation.
def foo():
    for i in range(10):
        time.sleep(1)
        print(1)

def fee():
    print('start task 1')
    time.sleep(5)
    print('task 1 done!')
    
def fees():
    print('start task 2')
    time.sleep(4)
    print('task 2 done!')

def main():
    fee()
    foo()
    fees()

main()
