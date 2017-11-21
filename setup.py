"""
Command Line Image Hash
"""
from setuptools import find_packages, setup

dependencies = ['click', 'Pillow', 'imagehash']

setup(
    name='imagehash-cli',
    version='0.1.0',
    url='https://github.com/lunardog/imagehash-cli',
    license='MIT',
    author='Leszek Rybicki',
    author_email='leszek-rybicki@cookpad.com',
    description='Image Hash Command Line Interface',
    download_url='https://github.com/lunardog/imagehash-cli/archive/0.1.0.tar.gz',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    test_requires=dependencies,
    entry_points={
        'console_scripts': [
            'imagehash = imagehash_cli.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
