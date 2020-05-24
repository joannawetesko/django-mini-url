import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django-mini-url',
    version='1.0',
    packages=['miniurl'],
    include_package_data=True,
    install_requires=['hashids', 'django', 'gunicorn', 'django-heroku'],
    license='Apache 2.0 License',
    description='A Basic URL shortener for Django',
    long_description=README,
    url='https://github.com/joannawetesko/django-mini-url',
    author='Joanna Wetesko',
    author_email='joannawetesko@gmail.com',
    keywords=['django url shortener', 'django link shortener', 'url shortener', 'link shortener'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)