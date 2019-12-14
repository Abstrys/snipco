# makefile for snipco.

install:
	./setup.py install --user

clean:
	./setup.py clean --all

spotless:
	rm -rf build dist snipco.egg-info

build: spotless
	./setup.py build sdist

upload: build
	twine upload dist/*
