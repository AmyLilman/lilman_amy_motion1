while (true) {
    console.log(input.acceleration(Dimension.X))
    if (input.acceleration(Dimension.X) > 7 || input.acceleration(Dimension.X) < -7) {
        light.showAnimation(light.rainbowAnimation, 500)
    } else {
        // music.play_melody("C C G G A A G F F E E D D C G G F F E E D G G F F E E D C C G G A A G F F E E D D C ", 150)
        light.clear()
    }
    
}
