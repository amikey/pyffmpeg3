#!/usr/bin/env python3
from setuptools import setup, find_packages, Extension

import numpy as np
import pkgconfig
name = 'pyffmpeg'

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['numpy', ]
test_requirements = ['pytest', ]

ext_modules = []
for module in ['avcodec']:
    pkg = pkgconfig.parse('lib' + module)
    cflags = pkgconfig.cflags('lib' + module)
    ext = Extension('pyffmpeg._libavcodec_c',
                    sources=[name + '/lib' + module +'.i'],
                    include_dirs=[np.get_include()] + pkg['include_dirs'],
                    libraries=[module],
                    library_dirs=pkg['library_dirs'],
                    swig_opts=['-modern', '-py3', '-noolddefs',
                               '-relativeimport',
                               cflags]
                    )
    ext_modules.append(ext)

def get_version_and_cmdclass(package_path):
    import os
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location('version',
                                   os.path.join(package_path, '_version.py'))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__, module.cmdclass

version, cmdclass = get_version_and_cmdclass('pyffmpeg')

setup(
    author="Mark Harfouche",
    author_email='mark.harfouche@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python FFmpeg bindings for fast video encoding and decoding",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='pyffmpeg',
    name='pyffmpeg',
    packages=find_packages(include=['pyffmpeg']),
    ext_modules=ext_modules,
    tests_require=test_requirements,
    url='https://github.com/hmaarrfk/pyffmpeg',
    version=version,
    cmdclass=cmdclass,
    zip_safe=False,
)
