blink1py
========

Blink(1) python library

Prerequesites
-------------

1. Make the blink1 library (see [blink1/commandline](https://github.com/todbot/blink1/tree/master/commandline))

2. Rename the blink1 library to `libblink1.so.0.0` (or something that
will resolve as blink1) and add it to your path

Usage
-----

Example:

    blink1 = open_blink1()

    blink1.set_rgb(255, 0, 0)

    blink1.on() #white

    blink1.off()

    blink1.close()


Now with more with!

    with blink1py.open_blink1() as blink1:
        blink1.on()

