# MQC2
Video and Audio Video Quality Checks
1.run pip3 install -r requirements.txt 
2.pm2 start pm2/pm2_config.json

Check logs
pm2 logs



Installation steps:

Create logs, tmp folder inside the MQC2 dir.
Create videos folder outside MQC2 dir

sudo yum group install "Development Tools" -y 


FFMPEG INSTALLATION IN LINUX:
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xf ffmpeg-release-amd64-static.tar.xz
cd ffmpeg-release-amd64-static
sudo cp ffmpeg /usr/bin/
sudo cp ffprobe /usr/bin/

PM2 INSTALLATION:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
. ~/.nvm/nvm.sh
nvm install node
node -e "console.log('Running Node.js ' + process.version)"
npm install pm2@latest -g


Alternative PM2 installation incase above doesn't work
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash  
source ~/.bashrc
nvm install node 
nvm install lts/* 
npm install pm2@latest -g


SoundFile module:
sudo yum -y install libsndfile


OpenCV Issues:
https://itsmycode.com/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directory/


