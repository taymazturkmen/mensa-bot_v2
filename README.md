# Mensa Bot

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

A Discord bot that lists Caffeteria Menu

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

discord.py
requests
```
pip install discord.py
pip install requests
```

### Installing

You need to create a bot in https://discord.com/developers and copy your client secret and add it to your environment arguments.
To add your secret in terminal :
```
export BOT_TOKEN = yourClientSecretHere
```
## Usage <a name = "usage"></a>

```
python main.py
```
default prefix is ! and bot is used with !mensa , the changing of prefix is currently not allowed but it is on my to do list.