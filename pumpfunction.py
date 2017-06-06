def run_pump():
    a.pinMode(4,a.OUTPUT) #pump output 1
    a.pinMode(5,a.OUTPUT) #pump output 2
    a.pinMode(6,a.INPUT) #limit switch input pump 1
    a.pinMode(7,a.INPUT) #limit switch input pump 2
    pump1_ref = a.digitalRead(6)
    pump2_ref = a.digitalRead(7)
    if pump1_ref == LOW:
        a.digitalWrite(4,a.LOW)
        f.write("Digital Pump Output 1 relay is closed, pump running for 30 sec")
        print ("Digital Pump Output 1 relay is closed, pump running for 30 sec")
        time.sleep(30)
    elif pump2_ref == LOW:
        a.digitalWrite(5,a.HIGH)
        f.write("Digital Pump Output 1 relay is closed, pump running for 30 sec")
        print ("Digital Pump Output 1 relay is closed, pump running for 30 sec")
        time.sleep(30)
    else:
        f.write("Refill Reservoirs to continue watering plants")
        print ("Refill Reservoirs to continue watering plants")
        

    
