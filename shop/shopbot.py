import praw
import json
import time
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "shoppbot42@gmail.com"
receiver_email = "az359@cornell.edu"
password = "shopbot123"
# Create a secure SSL context
context = ssl.create_default_context()

starttime = time.time()
r = praw.Reddit(
    client_id="sHRWmKD0jm8F4g",
    client_secret="jvAX4MQ1LhN_TEAOFDJunyrdaIt4OQ",
    redirect_uri="http://localhost:8080",
    user_agent="shoppbot"
)

def browse ():
    neweststernglas = ""
    newestjunghans = ""
    newestdac = ""
    newestandro = ""
    watches = r.subreddit("watchexchange")
    audio = r.subreddit("avexchange")
    while True:
        for i in watches.search(query="sternglas", sort="new", limit=1):
            if i.title != neweststernglas:
                neweststernglas = i.title
                print(i.title)

                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email,
                    neweststernglas.encode("ascii", "ignore"))
        for i in audio.search(query="rme", sort="new", limit=1):
            if i.title != newestdac:
                newestdac = i.title
                print(i.title)
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  # Can be omitted
                    server.starttls(context=context)
                    server.ehlo()  # Can be omitted
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email,
                    newestdac.encode("ascii", "ignore"))

        for i in watches.search(query="junghans", sort="new", limit=1):
            if i.title != newestjunghans:
                newestjunghans = i.title
                print(i.title)

                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls(context=context)
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email,
                    newestjunghans.encode("ascii", "ignore"))
        time.sleep(15.0 - ((time.time() - starttime) % 15.0))

def retrier ():
    try:
        browse ()
    except:
        print("retrying")
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))
        retrier ()
        
retrier ()
