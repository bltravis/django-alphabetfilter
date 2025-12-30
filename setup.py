import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except:
        return ''

DESC = " ".join(__import__('alphafilter').__doc__.splitlines()).strip()

setup(
    name="django-alphafilter",
    version=__import__('alphafilter').get_version().replace(' ', '-'),
    url='http://github.com/coordt/django-alphabetfilter',
    author='Corey Oordt',
    author_email='coreyoordt@gmail.com',
    description=DESC,
    long_description=read_file('README.rst'),
    packages=find_packages(exclude=['example*']),
    license='Apache 2.0',
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
)
