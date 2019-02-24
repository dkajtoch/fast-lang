from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# model location
# https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz

__version__ = '0.1'

setup(
    name='fastlang',
    version=__version__,
    author='Dariusz Kajtoch',
    author_email='dkajtoch@gmail.com',
    description='FastText language detection tool.',
    keywords="fastText, language detection, NLP",
    url='https://github.com/dkajtoch/fast-lang',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    install_requires=['pybind11>=2.2', "setuptools>=0.7.0", "fasttext>=0.8.22"],
    python_requires=">=3.4",
    packages=[
        str('fastlang'),
        str('fastlang.tests'),
    ],
    package_dir = {"fastlang": "fast-lang"},
    package_data={'fastlang': ['data/*', 'model/*']},
    zip_safe=False,
    include_package_data=True,
)
