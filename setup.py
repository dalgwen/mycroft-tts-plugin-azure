#!/usr/bin/env python3
from os.path import join, abspath, dirname
from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

PLUGIN_ENTRY_POINT = 'ovos-tts-plugin-azure = ovos_tts_plugin_azure:AzureTTSPlugin'
setup(
    name='ovos-tts-plugin-azure',
    version='0.1',
    description='A tts plugin for OpenVoiceOS, using Azure Cognitive Services',
    long_description=README,
    long_description_content_type="text/markdown",
    url='http://github.com/dalgwen/ovos-tts-plugin-azure',
    author='Gwendal Roulleau',
    author_email='private@private.org',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_azure'],
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
