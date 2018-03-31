
# Dependencies

sudo apt-get install -y python3-pip build-essential git python python-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev dirmngr

# Packages

Debian : sudo echo "deb http://ppa.launchpad.net/kivy-team/kivy/ubuntu trusty main" >> /etc/apt/sources.list && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A863D2D6

# Install

apt update & apt install python3-kivy


# Extras

pip3 install docutils pygments Cython

pip3 install --upgrade pip wheel setuptools docutils pygments Cython
