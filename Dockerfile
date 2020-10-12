FROM xnewbie/xbot:latest

# Clone Repo 
RUN git clone https://github.com/X-Newbie/XBOT.git -b master /app/xbot

# Wokrking Dir
WORKDIR /app/xbot/

# Copy Config To Working Dir
COPY ./config.py /app/xbot/xbotg

# Run
CMD ["python3","-m","xbotg"]
