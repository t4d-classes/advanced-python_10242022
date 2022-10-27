""" coroutine files """

import asyncio
import argparse
import aiofiles

async def main() -> None:
  
  parser = argparse.ArgumentParser(
    description="Output a file to the console"
  )
  parser.add_argument('file_path', type=str, help='file to output')
  args = parser.parse_args()
  print(args)

  async with aiofiles.open(args.file_path, encoding="UTF-8") as color_file:
    async for color in color_file:
      print(color.rstrip())


asyncio.run(main())