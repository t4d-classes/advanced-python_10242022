import asyncio
import time
from random import randint
import threading
import time

def delay() -> float:
  """ delay """
  return randint(1,10) / 2

def get_data_sync(task_num: int) -> None:
  """ get date """
  print(f"thread id: {threading.get_ident()}")
  print(f"starting get data {task_num}")
  time.sleep(delay())
  print(f"finished get data {task_num}")

async def get_data_async(task_num: int) -> None:
  """ get date """
  print(f"thread id: {threading.get_ident()}")
  print(f"starting get data {task_num}")
  await asyncio.sleep(delay())
  print(f"finished get data {task_num}")    


async def main() -> None:
  # get_data_sync(1)
  # get_data_sync(2)
  # get_data_sync(3)

  # await asyncio.gather(
  #   asyncio.to_thread(get_data_sync, 1),
  #   asyncio.to_thread(get_data_sync, 2),
  #   asyncio.to_thread(get_data_sync, 3)
  # )

  await asyncio.gather(
    get_data_async(1),
    get_data_async(2),
    get_data_async(3),
  )

  print("all done")


if __name__ == "__main__":

  start = time.perf_counter()
  asyncio.run(main())
  end = time.perf_counter()

  file_name = __file__.split("/", maxsplit=-1)[-1]
  time_elapsed = end - start
  print(f"{file_name} ran in {time_elapsed:0.2f} seconds")
