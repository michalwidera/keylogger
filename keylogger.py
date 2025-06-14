import keyboard as kb
import time
from time import time as now

mydict = {}

time_start = int(now() * 100000)

def keylog():
  log_f = open("log.txt", 'a')

  def on_action(key):
    # print(key.name, int(key.time * 100000), key.scan_code, key.event_type , key.to_json(ensure_ascii=False) )

    if key.event_type == "down":
       mydict[key.scan_code] = int(key.time * 100000)
    else:
       print( key.name , str(( mydict[key.scan_code] - time_start ) / 100 )+ "ms"  , str((int(key.time * 100000) - mydict[key.scan_code]) / 100) + "ms" )

    curr_time_since_epoch = time.time()
    curr_time = time.ctime(curr_time_since_epoch)
    
    # https://docs.python.org/3/library/time.html#time.perf_counter_ns
    log_f.write(str(curr_time) + " : " + str(time.perf_counter_ns()) + " : " + str(int(key.time * 100000)) + " : " + str(key) + "\n")
    log_f.flush()

  kb.hook(on_action)
  kb.wait('esc')
  log_f.close()

keylog()
