import asyncio

async def fetch_data():
    print('iniciando')
    await asyncio.sleep(2)
    print('terminado')
    return {'data': 1}
async def numeros():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    tarea1 = asyncio.create_task(fetch_data())
    tarea2 = asyncio.create_task(numeros())

    valor = await tarea1
    print(valor)
    await tarea2

asyncio.run(main())