# madalyn setup

## install sphinx

1. install swig

        aptitude -y install swig

1. install pyaudio

        aptitude -y install python-pyaudio

1. install spyrk

        pip install spyrk

1. install bison

        aptitude install bison

1. install pocketsphinx DO NOT DO THIS

        pip install pocketsphinx

1. install stuff

        wget http://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz
        tar -zxvf ./sphinxbase-5prealpha.tar.gz
        cd ./sphinxbase-5prealpha
        ./configure --enable-fixed
        make clean all
        make check
        sudo make install
        cd ~/

1. more stuff

        wget http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz
        tar -zxvf pocketsphinx-5prealpha.tar.gz
        cd ./pocketsphinx-5prealpha
        ./configure
        make clean all
        make check
        make install
        cd ~/

1. and more...

        wget http://www.speech.cs.cmu.edu/tools/product/1437257241_18899/9707.dic
        wget http://www.speech.cs.cmu.edu/tools/product/1437257241_18899/9707.lm
        cd ~/

1. environ

        export LD_LIBRARY_PATH=/usr/local/lib
