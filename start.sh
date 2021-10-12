echo "Cloning Repo...."
git clone https://github.com/ZauteKm/ids-Robot.git /ids-Robot
cd /ids-Robot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 -m bot.py
