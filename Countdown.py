import time


impuls=0

total_time = int(input("Enter the time in minutes"))
dif_periots = int(input("how much different periot do u want"))
        
the_time = int(total_time * 60)

period_list =[]

for i in range(1, dif_periots + 1):
    periots=int(input(" write the {}. periot in minutes".format(i)))
    period_list.append(periots)
    


total_period = 0 

for periots in range(0, len(period_list)):
    total_period = int(total_period + (period_list[periots] * 60))
        
period_times = int(the_time / total_period)
        
        #left_period = the_time % period_times

for i in range(0,dif_periots * (period_times + 1)):
    period_list.append(period_list[i])



for x in range(the_time, 0, -1):
 
    seconds = int(x % 60)
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)
     
    if x == the_time - (period_list[impuls] * 60):
        print("{} minute period has ended [{}. period]".format(period_list[impuls],impuls + 1))
        time.sleep(5)
        the_time = the_time - (period_list[impuls] * 60)
        impuls= impuls + 1
print("times up")
