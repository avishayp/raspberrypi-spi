# raspberrypi-spi
Tiny spi loopback test for the rpi

### Run on a fresh rpi

Prerequisites: ssh-able rpi running raspbian

1. Install raspbian https://downloads.raspberrypi.org/raspbian_lite_latest
2. ssh to the rpi
3. Install docker `curl -sSL https://get.docker.com | sh`
4. Add docker-compose `sudo apt-get install docker-compose`
5. Enable spi: uncomment the line `dtparam=spi=on` in `/boot/config.txt` 
6. Optionally also `modprobe spi-bcm28355` for the module to be enabled immediately
7. Test: `lsmod | grep spi`, output should look like
 ```
 spidev                 16384  6
spi_bcm2835            16384  0
```
8. Put spi in loopback mode by shorting GPIO pins 9 and 10
8. Clone this repo `sudo apt-get install -y git && git clone https://github.com/avishayp/raspberrypi-spi`
9. Run the test `cd raspberrypi-spi && docker-compose up`
10. Expected output:
```
spi_1  | spi mode: 0
spi_1  | bits per word: 8
spi_1  | max speed: 500000 Hz (500 KHz)
spi_1  |
spi_1  | FF FF FF FF FF FF
spi_1  | 40 00 00 00 00 95
spi_1  | FF FF FF FF FF FF
spi_1  | FF FF FF FF FF FF
spi_1  | FF FF FF FF FF FF
spi_1  | DE AD BE EF BA AD
spi_1  | F0 0D
```
