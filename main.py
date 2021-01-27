while True:
    print(input.rotation(Rotation.ROLL))
    if input.rotation(Rotation.PITCH) < 45:
        light.set_all(light.rgb(0, 0, 255))
