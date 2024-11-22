import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        print(f'Status: {response.status}')

async def main():
    url = 'https://www.grsu.by/'
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(500)]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())