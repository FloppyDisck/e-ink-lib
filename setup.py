from setuptools import find_packages, setup

setup(
	name='eink',
	packages=find_packages(include=['eink']),
	version='0.1.0',
	description='E-ink display library for waveshare screens',
	author='FloppyDisck',
	install_requires=['Pillow>=6.1.0','RPi.GPIO>=0.6.5','spidev>=3.4'],
)
