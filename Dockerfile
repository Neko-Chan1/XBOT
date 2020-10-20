# We're using prebuilt docker images
FROM xnewbie/xbot:latest

#
# Clone repo and prepare working directory
#
RUN git clone 'https://github.com/X-Newbie/XBOT.git' /root/xbotg
RUN mkdir /root/xbotg/bin/
WORKDIR /root/xbotg/

# Try Upgrade some requirements
RUN pip3 install -r requirements.txt --upgrade

# Starting Worker
CMD ["bash", "start"]

