import psutil
import sys
try:
  if str(sys.argv[1]) == 'cpu':
        print (psutil.cpu_times())
  elif str(sys.argv[1]) == 'mem':
        print (psutil.virtual_memory())
  else:
        print("Usage: system_ifno.py <command> [mem,cpu] ", e)
        sys.exit(0)
except TypeError as e:
    print("Usage: system_ifno.py <command> [mem,cpu] ", e)

