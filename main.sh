# install the websockets library
pip3 install websockets 
# This stuff sets up gems so they can be installed locally
export GEM_HOME=~/.gem
export PATH="$GEM_HOME/bin:$PATH"
# Clear the screen and run sockets.py
clear
python3 sockets.py