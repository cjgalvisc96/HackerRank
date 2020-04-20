for x in range(1,int(input())+1):
    print(((10**x - 1)//9)**2) 
    
"""
import asyncio

async def response(n: int) -> str:
    for i in range(2, n + 2):
        result = [i for i in range(1, i)] + [i for i in range(i-2, 0, -1)]
        print(int(''.join(map(str, result))))

if __name__ == "__main__":
    asyncio.run(response(int(input())))
"""