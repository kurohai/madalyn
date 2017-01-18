#!/usr/bin/env python

import sys
import os
import pyaudio
import wave
from pprint import pprint
from rc import decodeSpeech, recog, madalyn_go, RoomControl, record
import pocketsphinx as ps


if __name__ == '__main__':
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
    lmd   = '/srv/madalyn/0844.lm'
    dictd = '/srv/madalyn/0844.dic'
    log = '/srv/madalyn/output.log'
    config = ps.Decoder.default_config()
    config.set_string('-hmm', hmdir)
    config.set_string('-lm', lmd)
    config.set_string('-dict', dictd)
    # config.set_string('-logfn', log)
    # config.set_string('-keyphrase', 'jarvis')
    # config.set_float('-kws_threshold', 1e-40)

    speechRec = ps.Decoder(config)

    while True:
        wavfile = record(2)
        results = recog(wavfile, speechRec)
        if results:
            results = results.lower()
            print results
            
            if 'jarvis' in results or 'madalyn' in results:
                print 'got cmd start'
                results = recog(record(3), speechRec)
                if results:
                    results = results.lower()
                    print results
                    madalyn_go(results)

