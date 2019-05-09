from setuptools import setup


setup(
    name='rextester_py',
    version='0.0.2',
    url='https://github.com/nitanmarcel/rextester_py',
    license='MIT',
    author='nitanmarcel',
    author_email='nitan.marcel@gmail.com',
    description='Simple Python interface for rextester.com, using aiohttp/requests',
    long_description='Simple Python interface for rextester.com, using aiohttp/requests',
    packages=['rextester_py'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'aiohttp',
        'requests'],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'])
