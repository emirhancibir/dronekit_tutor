from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

iha = connect("127.0.0.1:14550",wait_ready= True)

def takeoff(irtifa):
    while iha.is_armable == True:
        iha.mode = VehicleMode("GUIDED")
    
        print(str(iha.mode)+ " moduna alindi")
        
        iha.armed = True

        while iha.armed is not True:
            print("IHA Arm Ediliyor !! ")
            time.sleep(0.5)
    
         
        print("IHA Arm Edildi")
       
        
        iha.simple_takeoff(irtifa)
        # time.sleep(2)

        while iha.location.global_relative_frame.alt < irtifa*0.5:
            print("Belirli irtifaya yükseliyor")

        
        break
    while iha.is_armable is not True:
        print("IHA Arm Edilemez !!")
        break

takeoff(10)

konum = LocationGlobalRelative(-35.36223253, 149.16506963, 20)

iha.simple_goto(konum)
