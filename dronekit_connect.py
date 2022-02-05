from dronekit import connect

drone = connect('127.0.0.1:14550',wait_ready=True)

print(f"Drone Arm Durumu : {drone.armed}")

# deniz seviyesine gore altitude
print(f"Global frame {drone.location.global_frame}")
 
# yerden yüksekliği 
print(f"Global relative frame {drone.location.global_relative_frame}")

print(f"İrtifa {drone.location.global_relative_frame.alt}")