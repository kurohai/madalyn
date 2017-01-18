#!/usr/bin/env python2
from pocketsphinx import *
import pyaudio
import sys

hmm = '/usr/local/share/pocketsphinx/model/en-us/en-us'
dic = '/srv/madalyn/0844.dic'
lm= '/srv/madalyn/0844.lm'



config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-lm', lm)
config.set_string('-dict', dic)
config.set_string('-logfn', '/srv/madalyn/output.log')

decoder = Decoder(config)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
in_speech_bf = True
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        try:
            if  decoder.hyp().hypstr != '':
                print 'Partial decoding result:', decoder.hyp().hypstr
        except AttributeError:
            pass
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                try:
                    if  decoder.hyp().hypstr != '':
                        print 'Stream decoding result:', decoder.hyp().hypstr
                except AttributeError:
                    pass
                decoder.start_utt()
    else:
        break
decoder.end_utt()
print 'An Error occured:', decoder.hyp().hypstr
