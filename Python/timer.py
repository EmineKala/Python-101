from pomodoro_bot import start_timer
import time
import datetime
from plyer import notification

class StopTimer:
   
   def __init__(self,work_time):
      self.start_time = datetime.datetime.now()
      self.work_time = work_time
 #print(start_time)
      time.sleep(self.work_time*5)
      print("Çalışma süreniz dolmuştur")

   def get_expire_time(self):
      invoke_time = datetime.datetime.now()
      return invoke_time - self.start_time

stop_timer(1)       
    

# asking_time = datetime.datetime.now()
# expire_time = asking_time - start_time
# print(expire_time.seconds)

# count = 0
# print("40 dakikalık çalışma seansı başladı. Çalışmaya başla!")

# while True:
#         time.sleep(2400)
#         count += 1
#         notification.notify(
#             title = "Tebrikler!",
#             message = f"10 dakika mola! {count}. çalışma seansı",
#         )
#         time.sleep(600)
#         notification.notify(
#             title = "Mola bitti. Çalışmaya geri dönmelisin!",
#             message = "Çalışma seansı başlatılıyor",
#         )
        
        