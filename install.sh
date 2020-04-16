#!/bin/bash
sudo apt-get install nodejs npm
git clone https://github.com/paulbroadmission/linebot_mem.git
cd /linebot_mem/src/frontend/vue_bot_UI
npm install
npm run serve
