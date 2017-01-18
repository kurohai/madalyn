from rc import recog


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

wavfile = 'fucking-goddamn-shit.wav'

print recog(wavfile, decoder)
