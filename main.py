

while True:
    print(input.acceleration(Dimension.X))
    if input.acceleration(Dimension.X) > 0 or input.acceleration(Dimension.X) < -20:
        light.show_animation(light.rainbowAnimation, 500)
        #music.play_melody("C C G G A A G F F E E D D C G G F F E E D G G F F E E D C C G G A A G F F E E D D C ", 150)
    else:
        light.clear()
        #music.stop_all_sounds()