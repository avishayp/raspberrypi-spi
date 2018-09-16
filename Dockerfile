FROM alpine:3.8

RUN apk add --no-cache \
	gcc \
	linux-headers \
	musl-dev \
	python3 \
	python3-dev

RUN cd /usr/bin \
	&& ln -s python3 python \
	&& ln -s pip3 pip

RUN pip install --no-cache \
	pip==18 \
	spidev

COPY spidev_test.c /home/
RUN gcc -o /usr/bin/spidev_test /home/spidev_test.c

CMD ["python"]
