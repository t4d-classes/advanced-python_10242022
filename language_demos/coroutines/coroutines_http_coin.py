""" coroutines http coin """

import asyncio
import aiohttp

async def main() -> None:
  

  url = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=litecoin%2Cbitcoin%2Cethereum&vs_currencies=usd,eur"
  )

  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      prices = await resp.json()
      print(prices)


asyncio.run(main())