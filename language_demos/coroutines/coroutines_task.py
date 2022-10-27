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
  
  task1 = asyncio.create_task(get_data(1))
  task2 = asyncio.create_task(get_data(2))
  task3 = asyncio.create_task(get_data(3))

  print(task1)
  print(type(task1))

  await task3
  print("task 3 is done")

  await task1
  print("task 1 is done")

  await task2
  print("task 2 is done")



if __name__ == "__main__":

  start = time.perf_counter()
  asyncio.run(main())
  end = time.perf_counter()

  file_name = __file__.split("/", maxsplit=-1)[-1]
  time_elapsed = end - start
  print(f"{file_name} ran in {time_elapsed:0.2f} seconds")
