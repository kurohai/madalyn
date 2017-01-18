from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

hmdir = '/usr/local/share/pocketsphinx/model/en-us/en-us'
lmd   = '/srv/madalyn/0844.lm'
dictd = '/srv/madalyn/0844.dic'


DATADIR = "/mnt/db/git"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', hmdir)
config.set_string('-lm', lmd)
config.set_string('-dict', dictd)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open('/mnt/db/git/jarvis.wav', 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
# print decoder.get_hyp()[0]
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
print ('Best hypothesis segments: ', [seg.prob for seg in decoder.seg()])
pprint(decoder.seg()[1])
