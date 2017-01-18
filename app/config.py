#!/usr/bin/env python


from secret import Secret


class Config(object):
    """docstring for Config"""

    spark_username = Secret.spark_username
    spark_password = Secret.spark_password

    hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
    lmd   = '/srv/madalyn/0844.lm'
    dictd = '/srv/madalyn/0844.dic'
    log = '/srv/madalyn/output.log'

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 6
