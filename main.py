#while True:
#    print(input.rotation(Rotation.PITCH))
#    if input.rotation(Rotation.PITCH) > 0 or input.rotation(Rotation.PITCH) < 0:
#        light.set_all(light.rgb(0, 0, 255))
#    else:
#        light.clear()

while True:
    print(input.acceleration(Dimension.Y))
    if input.acceleration(Dimension.Y) > 0 or input.acceleration(Dimension.Y) < 0:
        light.set_all(light.rgb(255, 0, 255))
    else:
        light.clear()
