import random

ride_wait_times = 42,10,25,18,33

Transition_1 = 0.23,0.33,0.52,0.75,1.00
Transition_2 = 0.12,0.19,0.37,0.79,1.00
Transition_3 = 0.30,0.38,0.54,0.78,1.00
Transition_4 = 0.40,0.52,0.67,0.76,1.00
Transition_5 = 0.09,0.18,0.46,0.57,1.00

i=0
last_ride = 3
elapsed_time = 0
time_total = 0

def nextride():
    global last_ride
    global elapsed_time
    if last_ride == 1:
        rand_ride = random.random()
        for i in range(len(Transition_1)):
            if rand_ride<Transition_1[i]:
                next_ride = i+1
                break
    elif last_ride == 2:
        rand_ride = random.random()
        for i in range(len(Transition_2)):
            if rand_ride<Transition_2[i]:
                next_ride = i+1
                break
    elif last_ride == 3:
        rand_ride = random.random()
        for i in range(len(Transition_3)):
            if rand_ride<Transition_3[i]:
                next_ride = i+1
                break
    elif last_ride == 4:
        rand_ride = random.random()
        for i in range(len(Transition_4)):
            if rand_ride<Transition_4[i]:
                next_ride = i+1
                break
    elif last_ride == 5:
        rand_ride = random.random()
        for i in range(len(Transition_5)):
            if rand_ride<Transition_5[i]:
                next_ride = i+1
                break
    if next_ride != last_ride:
        elapsed_time += 5
    elapsed_time += ride_wait_times[next_ride-1]
    #if k%10000 == 0:
    #    print(last_ride,"->",next_ride,",")
    last_ride = next_ride

def iterate():
    global elapsed_time
    elapsed_time = 5
    nextride()
    while last_ride != 3:
        nextride()
    #if k%10000 == 0:
    #    print("n")
    
for k in range(1000000):
    iterate()
    time_total += elapsed_time

print(float(time_total)/float(k+1))
