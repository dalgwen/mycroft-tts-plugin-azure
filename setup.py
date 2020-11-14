#!/usr/bin/env python3
from os.path import join, abspath, dirname
from setuptools import setup

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

PLUGIN_ENTRY_POINT = 'azure_tts = mycroft_tts_plugin_azure:AzureTTSPlugin'
setup(
    name='mycroft-tts-plugin-azure',
    version='0.1',
    description='A tts plugin for mycroft, using Azure Cognitive Services',
    url='http://github.com/dalgwen/mycroft-tts-plugin-azure',
    author='Gwendal Roulleau',
    author_email='private@private.org',
    license='Apache-2.0',
    packages=['mycroft_tts_plugin_azure'],
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.7',
    ],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
