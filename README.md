# pwd-raspi
My awesome remote control system for my Pinewood Derby car
[Pinewood Derby Logo](http://www.abc-pinewood-derby.com/images/pinewood-derby-logo.png)

Yes, it's a Cub Scout thing. I'm a Boy Scout, I used to be a Cub Scout, but my brother still is a Cub. There's an open race that anyone can participate in, and since it's the last chance I'd get, I am going out with a bang. Rather, a flash.

Not much in the `remote` directory, just a script that automatically `ssh`es to the Pi Zero on the car, and opens a `dtach` that is already running on there. The main program, that runs onboard the car, is in the `car` directory.

The theory is, I hit a number sequence on the keypad connected to my main Pi, next to the track, something like this:

1. I hit a number to specify the light color
2. Then, a number to specify which of that color to light
Here, a fancy chart:
| Light Color | Number |
| ----------- | ------ |
| Red | 1 |
| Yellow | 2 |
| Green | 3 |
| Blue | 4 |
2 of each color, so `1` or `2`

* To turn lights off:
|Number|Action|
|0|Turn specified color off|
|8|Turn all lights off|


