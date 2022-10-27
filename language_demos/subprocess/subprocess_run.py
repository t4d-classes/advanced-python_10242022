import subprocess

result = subprocess.run(
    "where chkdsk.exe",
    shell=True,
    capture_output=True,
    text=True)

print(f"result: {result}")
print(f"return code: {result.returncode}")

print(result.stdout)

