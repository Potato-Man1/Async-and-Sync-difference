import asyncio
#To inicate that the function coroutine we must add async before the def
async def foo():
    for i in range(10):
        #Await means to wait until that line of code is finished
        #Note that we can only put await if it's in a coroutine function
        await asyncio.sleep(1)
        print(1)

async def fee():
    print('start task 1')
    #Once again asyncio.sleep is just imitating an action that takes time to get done
    await asyncio.sleep(5)
    #after a certain amont of time this will indicate if it's finished 
    print('task 1 is done!')
    
async def fee():
    print('start task 2')
    await asyncio.sleep(4)
    print('task 2 done!')
    

async def main():
    #with task it can switch between them if the current function is not needed to run
    task1 = asyncio.create_task(fee())
    task2 = asyncio.create_task(foo())
    task3 = asyncio.create_task(fees())
    #This await lines on the task is an indicator that it must finish it, If you didn't add awaits the functions will not be finished
    await task2
    await task1
    await task3
    
#To run a async function use asyncio.run
asyncio.run(main())
