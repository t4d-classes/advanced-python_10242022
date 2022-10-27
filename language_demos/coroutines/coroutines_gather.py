import asyncio
import aiofiles
import time
from random import randint

def delay() -> float:
  """ delay """
  return randint(1,10) / 2


counter = 0  


async def get_data(task_num: int) -> None:
  """ get date """
  global counter
  counter += 1
  print(f"starting get data {task_num}", counter)
  await asyncio.sleep(delay())
  print(f"finished get data {task_num}", counter)
  counter -= 1

# code related to a question about processing lots of files...
# async def load_and_process_array_file(file_name):
#   async with aiofiles.open(file_name, encoding="UTF-8") as color_file:
#     file_contents = await color_file.read_file()
#     # more code to process file contents
#     cleaned_up_file_contents = file_contents
#     return cleaned_up_file_contents


# async def load_array_files():

#   file_nums = range(52)

#   file_results = await asyncio.gather(*[load_and_process_array_file(f"{file_num}.txt") for file_num in file_nums ])

#   # this is what you would operate on all of the together



async def main() -> None:
  
  await asyncio.gather(get_data(1), get_data(2), get_data(3))


if __name__ == "__main__":

  start = time.perf_counter()
  asyncio.run(main())
  end = time.perf_counter()

  file_name = __file__.split("/", maxsplit=-1)[-1]
  time_elapsed = end - start
  print(f"{file_name} ran in {time_elapsed:0.2f} seconds")
