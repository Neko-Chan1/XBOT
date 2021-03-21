# We're using prebuilt docker images
FROM userindobot/docker:ubotindo

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/Neko-Chan1/XBOT /root/xbot
RUN mkdir /root/xbot/bin/
WORKDIR /root/xbot/

RUN pip install -U pip

# Try Upgrade some requirements
RUN pip3 install -r requirements.txt

# Run
CMD ["bash", "start"]
