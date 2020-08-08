import asyncio
import aiohttp
from random import randint


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


async def doRequestGET(session, n):
    url = "this will be the url"
    print("making request {n} to {url}")
    async with session.get(url) as resp:
        print(await resp.text())

async def doRequestPOST(session, n):
    async with session.post(
            url="sample url",
            json={
                "sample": "this is sample"}) as resp:
            print(await resp.text())

async def main():
    n = 5
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[doRequestPOST(session, i) for i in range(n)]
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
