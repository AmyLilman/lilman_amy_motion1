#while True:
#    print(input.rotation(Rotation.PITCH))
#    if input.rotation(Rotation.PITCH) > 0 or input.rotation(Rotation.PITCH) < 0:
#        light.set_all(light.rgb(0, 0, 255))
#    else:
#        light.clear()

#while True:
#    print(input.acceleration(Dimension.Y))
#    if input.acceleration(Dimension.Y) > 0 or input.acceleration(Dimension.Y) < 0:
#        light.set_all(light.rgb(255, 0, 255))
#    else:
#        light.clear()

while True:
    print(input.acceleration(Dimension.X))
    if input.acceleration(Dimension.X) > 0 or input.acceleration(Dimension.X) < -20:
        light.show_animation(light.rainbowAnimation, 500)
        music.play_melody("C C G G A A G F F E E D D C G G F F E E D G G F F E E D C C G G A A G F F E E D D C ", 150)
    else:
        light.clear()
        music.stop_all_sounds()