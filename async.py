import asyncio
#Once again asyncio.sleep is just imitating an action that takes time to get done
async def foo():
    for i in range(10):
        await asyncio.sleep(1)
        print(1)

async def fee():
    print('start task 1')
    await asyncio.sleep(5)
    print('task 1 is done!')
    
async def fees():
    print('start task 2')
    await asyncio.sleep(4)
    print('task 2 done!')
    

async def main():
    task1 = asyncio.create_task(fee())
    task2 = asyncio.create_task(foo())
    task3 = asyncio.create_task(fees())
    await task2
    await task1
    await task3
    
asyncio.run(main())
