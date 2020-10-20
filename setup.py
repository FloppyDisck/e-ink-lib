from setuptools import find_packages, setup

setup(
	name='eink',
	packages=['eink'],
	version='0.1.0',
	license='MIT',
	description='E-ink display library for waveshare screens',
	author='FloppyDisck',
	author_email='guy.garcia@upr.edu',
	url = 'https://github.com/FloppyDisck/e-ink-lib',
	download_url='',
	keywords = ['waveshare', 'eink', 'e-ink'],
	install_requires=['Pillow>=6.1.0','RPi.GPIO>=0.6.5','spidev>=3.4'],
	classifiers=[
	    'Development Status :: 5 - Production/Stable',
	    'Intended Audience :: Developers',
	    'Topic :: Software Development :: Build Tools',
	    'License :: OSI Approved :: MIT License',
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6',
	  ],
	packages=find_packages(include=['eink']),
)
