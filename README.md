#Telegram Bot with Local LLM Integration

This project is a Telegram bot that uses a locally hosted Large Language Model (LLM) via LM Studio and integrates it through AnythingLLM for API-based communication.

For the test with bots, I experimented with kldlm, for example you can write wether and ask him the current Wether 

Python 3.10 or higher
A Telegram account
LM Studio (for running the local LLM)
AnythingLLM (to provide an API interface for the LLM)

Setup Instructions

1)Create a Telegram Bot
    -Go to https://t.me/botfather on Telegram
    -Create a new bot and replace telegram_bot_token
    
2)Download and Run LM Studio
    -Install LM Studio from https://lmstudio.ai/
    -Download a language model 
    -Launch the model and make sure it's running locally 
    
3)Install and Configure AnythingLLM
    -Clone the AnythingLLM 
    -Follow the setup instructions
    -Open http://localhost:7070 in your browser 
    (I used docker to bring it up, I did it on linux)
    export STORAGE_LOCATION=$HOME/anythingllm && \
    mkdir -p $STORAGE_LOCATION && \
    touch "$STORAGE_LOCATION/.env" && \
    docker run -d -p 3001:(the port you want to use (example 7070)) \
    --cap-add SYS_ADMIN \
    -v ${STORAGE_LOCATION}:/app/server/storage \
    -v ${STORAGE_LOCATION}/.env:/app/server/.env \
    -e STORAGE_DIR="/app/server/storage" \
    mintplexlabs/anythingllm
    (For Windows)
    $env:STORAGE_LOCATION="$HOME\Documents\anythingllm"; `
    If(!(Test-Path $env:STORAGE_LOCATION)) {New-Item $env:STORAGE_LOCATION -ItemType Directory}; `
    If(!(Test-Path "$env:STORAGE_LOCATION\.env")) {New-Item "$env:STORAGE_LOCATION\.env" -ItemType File}; `
    docker run -d -p 3001:(the port you want to use (example 7070))`
    --cap-add SYS_ADMIN `
    -v "$env:STORAGE_LOCATION`:/app/server/storage" `
    -v "$env:STORAGE_LOCATION\.env:/app/server/.env" `
    -e STORAGE_DIR="/app/server/storage" `
    mintplexlabs/anythingllm;
    -Connect AnythingLLM to your running LM Studio instance
    
4)Generate an API Key in AnythingLLM
    -Use the AnythingLLM web interface to generate an API key
    -Copy this key and replace api_key
    -Create a workspace named firstworkspace (Example http://localhost:7070/api/v1/workspace/firstworkspace/chat)
    You can choose a different name, but then you'll have to change it in the link as well.

That's the end of it, now you will have a neural network running locally on your computer and your telegram bot will have access to it, your smart bot :)

