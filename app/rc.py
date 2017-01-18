
import pocketsphinx as ps
import sphinxbase
import sys
import os
import pyaudio
import wave
from pprint import pprint
from spyrk import spark_cloud


spark = None

def decodeSpeech(wavfile, speechRec):

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
    if r:
        return r.hypstr


def record(seconds):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = seconds

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

def recog(wavfile, speechRec):
    return decodeSpeech(wavfile, speechRec)

def madalyn_go(r):
    cmd = r.lower()
    # print r
    # if r.startswith('jarvis') or r.startswith('madalyn'):
    # cmd = r.split(' ')
    if 'light' in cmd or 'fan' in cmd:
        cmd = cmd.replace('light', '')
        cmd = cmd.replace('fan', '')
        if 'one' in cmd:
            cmd = cmd.replace('one', '')
            if 'on' in cmd:
                print('light one is now on!')
                null = RoomControl('D1', 1)
            elif 'off' in cmd:
                print('light one is now off!')
                null = RoomControl('D1', 0)
        elif 'two' in cmd:
            cmd = cmd.replace('two', '')
            if 'on' in cmd:
                print('light two is now on!')
                null = RoomControl('D2', 1)
            elif 'off' in cmd:
                print('light two is now off!')
                null = RoomControl('D2', 0)



def RoomControl(target, state):
    pprint(spark.devices['spark-01'].connected)
    if state == 1:
        spark.devices['spark-01'].digitalwrite(target, 'HIGH')
    else:
        spark.devices['spark-01'].digitalwrite(target, 'LOW')

