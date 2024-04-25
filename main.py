from djitellopy import Tello

drone = Tello()

drone.connect()

drone.takeoff()

for i in range(4):
  drone.move_forward(130)
  drone.rotate_clockwise(90)

drone.land()

drone.end()
