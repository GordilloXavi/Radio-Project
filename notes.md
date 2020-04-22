ssh as root:
`ssh root@134.209.192.226`

# Firewall:
See apps:
`ufw app list`
Add new rule:
`ufw {allow|deny} <app_name>`
Check current rules:
`ufw status`
Delete existing rule:
`uf delete {allow|deny} <app_name>`

# Nginx
Check server status:
`systemctl status nginx`
Reload Nginx (to apply config changes):
Check the syntax of the config files first:
`nginx -t`
`systemctl reload nginx`

# SSL Certificate:
```
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/xgordillo.dev/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/xgordillo.dev/privkey.pem
   Your cert will expire on 2020-07-05. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
```

# Postgres shell:
Open a psql interactive terminal:
`psql --host=<host> --username=<username> --dbname=<dbname>`
You will be prompted to imput the password specified in $POSTGRES_PASSWORD
Show all relations in current database:
`\d`
Use expanded display (pretty output):
`\x`

# DOCKER:
Copy local file to container:
`docker cp <file> hotbox-app:/app/<file>`


# Important links:
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04?utm_source=local&utm_medium=Email_Internal&utm_campaign=Email_UbuntuDistroNginxWelcome&mkt_tok=eyJpIjoiTTJFd1pXWmhZamt4TnpRdyIsInQiOiJrYWlpVlRlTWFmUkg5SnZVYmxVUjk0dUEwMXd3YUdrc2N5K08rUlhDT2xPMUIxS1BnZFVlQ3V6dUxNRXQrN2tMbXBJVms2VVNrdlAybmw3c2hNemlaWUFWZ1p3Q24rV2xnNzg2VGM2azFnSm8wcncwQ0xDK09cL2ZkMFA5UzNMdXcifQ%3D%3D

SSL Configuration:
https://www.digitalocean.com/community/tutorials/como-asegurar-nginx-con-let-s-encrypt-en-ubuntu-18-04-es
