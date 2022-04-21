# MQC2
Video and Audio Video Quality Checks
1.run pip3 install -r requirements.txt 
2.pm2 start pm2/pm2_config.json

Check logs
pm2 logs



Installation steps:

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


SoundFile module:
sudo yum -y install libsndfile



