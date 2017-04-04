# Mastodon Tooter Bot

A dead simple Mastodon bot that posts (toots) a list of phrases from a text file.

## Registering a new bot

1. Create an account on the Mastodon instance you wish to post to.
2. Register the app with Mastodon. The best method to register for using this app is via the [Mastodon.py API](http://mastodonpy.readthedocs.io/en/latest/#). If you using any other method, you'll need to create your own client credentials file (your client ID and client secret on separate lines).
3. Get your OAuth access token. Similarly to the above, the best method to get this is via the Mastodon.py API. If you use any other method, you'll need to create your own user credentials file (just your raw access token string).

## Usage

    usage: bot.py [-h] [--user USER] [--client CLIENT] [--toot TOOT] [--debug]
                  file

    A dead simple Mastodon bot that posts (toots) a list of phrases from a text
    file.

    positional arguments:
      file             Path to the list of phrases to toot. Will toot in line
                       order. Required.

    optional arguments:
      -h, --help       show this help message and exit
      --user USER      Path to the file containing your client ID and client
                       secret. (default: ./usercred.txt)
      --client CLIENT  Path to the file containing your access token. (default:
                       ./clientcred.txt)
      --toot TOOT      Toot a single phrase.
      --debug          Outputs debug info to stdout. Optional
