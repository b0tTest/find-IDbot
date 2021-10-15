echo "Cloning Repo...."
git clone https://github.com/b0tTest/find-IDbot.git /find-IDbot
cd /find-IDbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
