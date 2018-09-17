FROM avishayp/spidev_test

RUN apk add --update --no-cache \
	python3 \
	python3-dev

RUN cd /usr/bin \
	&& ln -s python3 python \
	&& ln -s pip3 pip

RUN pip install --no-cache \
	pip==18 \
	spidev

CMD ["python"]
