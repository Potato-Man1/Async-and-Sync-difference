import time
#The sleep is just copying an action that takes some time to finish
def foo():
    for i in range(10):
        time.sleep(1)
        print(1)

def fee():
    print('start')
    time.sleep(5)
    print('done!')
    
def fees():
    print('starts')
    time.sleep(4)
    print('dones!')
    

def main():
    fee()
    foo()
    fees()

main()
