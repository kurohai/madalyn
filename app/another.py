import sys, os, pyaudio
from pocketsphinx import *
from rc import madalyn_go, RoomControl


# Create a decoder with certain model
keyword = 'JARVIS'
config = Decoder.default_config()

hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
lmd   = '/srv/madalyn/2042.lm'
dictd = '/srv/madalyn/2042.dic'
log = '/srv/madalyn/output.log'
config.set_string('-hmm', hmdir)
config.set_string('-lm', lmd)
config.set_string('-dict', dictd)
config.set_string('-logfn', log)

decoder = Decoder(config)
decoder.start_utt()

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

RoomControl('D0', 1)

while True:
    try:
        buf = stream.read(512)
        decoder.process_raw(buf, False, False)
        words = decoder.hyp().hypstr.split(' ')
        print len(words)


        if decoder.hyp() != None and keyword in decoder.hyp().hypstr:
            print 'Jarvis is ready...'
            speech = decoder.hyp().hypstr
            words = speech.split(' ')

            # only use last ten words spoken
            if len(words) >= 10:
                print words
                command = ' '.join([x for x in words[-10:]])
            else:
                print words
                command = ' '.join([x for x in words])

            print 'running command:', command
            madalyn_go(command)
            decoder.end_utt()
            decoder.start_utt()

    except KeyboardInterrupt as e:
        print e
        RoomControl('D0', 0)
        sys.exit(0)
    except Exception as e:
        print e
