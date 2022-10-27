import asyncio
import time
from random import randint

def delay() -> float:
  """ delay """
  return randint(1,10) / 2


async def get_data(task_num: int) -> None:
  """ get date """
  print(f"starting get data {task_num}")
  await asyncio.sleep(delay())
  print(f"finished get data {task_num}")


async def main() -> None:
  
  await get_data(1)
  await get_data(2)
  await get_data(3)


if __name__ == "__main__":

  start = time.perf_counter()
  asyncio.run(main())
  end = time.perf_counter()

  file_name = __file__.split("/", maxsplit=-1)[-1]
  time_elapsed = end - start
  print(f"{file_name} ran in {time_elapsed:0.2f} seconds")
