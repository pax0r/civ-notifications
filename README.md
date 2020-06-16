Civilization VI discord notifications
=====================================

Simple Django app to show who's turn it is and send some notification on Discord channel.

## Deployment

App can be easy deployed using attached `docker-compose.yml` file. 
There is a simple script `docker-run-build.sh` which will build and run everything from single command.

Some env variables needs to best prior deploying the stack.
See attached `.env.example` file for details. 
One simply needs to copy `.env.example` to `.env` and fill proper variables.

After that it is enough to run `docker-compose up -d`. It will deploy three docker containers:
1) `uwsgi` with Application and single worker
2) `postgresql` database
3) `redis` instance for RQ

By default `uwsgi` exposes the application through `uwsgi` protocol so you need a reverse proxy nginx to 
forward requests to Docker container. 

## Civilization VI webhook

To use application one needs to simply set a webhook endpoint at Civilization VI game setting to:
```
http://<your-host-name>/webhook/
```
**WARNING:** For some reason Civilization VI does not send proper webhooks for `https` endpoints so sadly you NEED TO use `http`.
Feel free to configure your webserver to redirect every other url to `https`.


## Discord notifications

Discord notifications can be configured via Django Admin panel. 
After the first web hook from Civilization server you should see a Game instance in the Django Admin panel.
Create Discord Webhook Bot and put details in the Admin panel.

### Player mapping

One can configure mapping of Discord users to player names so Discord notification will `@mention` given user.

To do so one needs to put `discord_id` in admin panel which can be obtained by issuing `\@username` at Discord channel.