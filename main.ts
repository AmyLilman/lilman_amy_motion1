while (true) {
    console.log(input.rotation(Rotation.Roll))
    if (input.rotation(Rotation.Pitch) > 0) {
        light.setAll(light.rgb(0, 0, 255))
    } else {
        light.clear()
    }
    
}
