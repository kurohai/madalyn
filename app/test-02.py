#!/usr/bin/env python


# import sys
# import os
# import pyaudio
# import wave
# from pprint import pprint
# from spyrk import spark_cloud
from config import Config


hmdir = Config.hmdir
lmd = Config.lmd
dictd = Config.dictd
log = Config.log

# spark = spark_cloud.SparkCloud(Config.spark_username, Config.spark_password)

CHUNK = Config.CHUNK
FORMAT = Config.FORMAT
CHANNELS = Config.CHANNELS
RATE = Config.RATE
RECORD_SECONDS = Config.RECORD_SECONDS


def decodeSpeech(hmmd, lmdir, dictp, wavfile):

    import pocketsphinx as ps
    import sphinxbase

    config = ps.Decoder.default_config()
    config.set_string('-hmm', hmmd)
    config.set_string('-lm', lmdir)
    config.set_string('-dict', dictp)
    config.set_string('-logfn', log)
    speechRec = ps.Decoder(config)

    # print(help(ps.Decoder))
    # speechRec = ps.Decoder(
        # hmm=hmmd,
        # lm = lmdir,
        # dict = dictp
    # )
    # speechRec.lm = lmdir

    wavFile = file(wavfile,'rb')
    wavFile.seek(44)

    speechRec.start_utt()
    while True:
        buf = wavFile.read(1024)
        if buf:
            speechRec.process_raw(buf, False, False)
        else:
            break

    speechRec.end_utt()
    r = speechRec.hyp()

    return r.hypstr


def record():
    fn = 'o.wav'
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print('* recording')
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print('* done recording')
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return fn


def recog(wavfile):
    recognised = decodeSpeech(hmdir, lmd, dictd, wavfile)
    return recognised


def madalyn_go(r):
    r = r.lower()
    print(r)
    if r.startswith('jarvis') or r.startswith('madalyn'):
        cmd = r.split(' ')
        if cmd[1] == 'set':
            if cmd[2] == 'light':
                if cmd[3] == 'one':
                    if cmd[4] == 'on':
                        print('light one is now on!')
                        null = RoomControl('D1', 1)
                    if cmd[4] == 'off':
                        print('light one is now off!')
                        null = RoomControl('D1', 0)


def RoomControl(target, state):
    pprint(spark.devices['spark-01'].connected)
    if state == 1:
        spark.devices['spark-01'].digitalwrite(target, 'HIGH')
    else:
        spark.devices['spark-01'].digitalwrite(target, 'LOW')


if __name__ == '__main__':
    wavfile = record()
    # wavfile = 'o.wav'
    result = recog(wavfile)
    madalyn_go(result)
