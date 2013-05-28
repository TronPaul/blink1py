import blink1_raw as b1raw

def open_blink1(id=None, serial=None, path=None):
    if id is not None:
        blink1 = b1raw.open_by_id(id)
    elif serial is not None:
        blink1 = b1raw.open_by_serial(serial)
    elif path is not None:
        blink1 = b1raw.open_by_path(path)
    else:
        blink1 = b1raw.blink1_open()
    return Blink1(blink1)

def close_blink1(blink1):
    b1raw.blink1_close(blink1)

class Blink1(object):
    def __init__(self, device):
        self._device = device
        self.__closed = False

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    def __del__(self):
        try:
            self.close()
        except:
            pass

    def close(self):
        if not self.__closed:
            try:
                close_blink1(self._device)
            finally:
                self.__closed = True

    def play(self, pos=0):
        b1raw.play(self._device, 1, pos)

    def stop(self, pos=0):
        b1raw.play(self._device, 0, pos)

    def set_pattern(self, pos, r=0, g=0, b=0, time=0):
        b1raw.write_pattern_line(self._device, time, r, g, b, pos)

    def read_pattern(self, pos):
        time, r, g, b = b1raw.read_pattern_line(self._device, pos)
        return r, g, b, time

    def off(self):
        self.set_rgb(0, 0, 0)

    def on(self):
        self.set_rgb(255, 255, 255)

    def set_rgb(self, r=0, g=0, b=0):
        self.fade_rgb(r, g, b)

    def fade_rgb(self, r=0, g=0, b=0, time=0):
        if not time:
            b1raw.set_rgb(self._device, r, g, b)
        else:
            b1raw.fade_to_rgb(self._device, time, r, g, b)
