while True:
    if input.rotation(Rotation.PITCH) > 20:
        light.set_all(light.rgb(0, 0, 255))