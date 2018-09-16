#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
simplified version of https://github.com/torvalds/linux/blob/master/tools/spi/spidev_test.c for py-spidev
"""

import spidev

test_payload = [
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0x40, 0x00, 0x00, 0x00, 0x00, 0x95,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
    0xDE, 0xAD, 0xBE, 0xEF, 0xBA, 0xAD,
    0xF0, 0x0D
]

max_speed = 500000

# for printing only
arr_size = 6


def main(bus, dev):
    with spidev.SpiDev() as s:
        s.open(bus, dev)
        s.max_speed_hz = max_speed
        print("spi mode: %d" % s.mode)
        print("bits per word: %d" % s.bits_per_word)
        print("max speed: %d Hz (%d KHz)\n" % (s.max_speed_hz, s.max_speed_hz // 1000))

        res = s.xfer(test_payload)
        assert any(res), "spi loopback read all zeros: make sure pins GPIO-10 & GPIO-9 are shorted! (jumped)"
        assert res == test_payload
        for chunk in range(0, len(res), arr_size):
            print(' '.join(format(r, '02X') for r in res[chunk:chunk + arr_size]))


if __name__ == '__main__':
    main(bus=0, dev=0)
