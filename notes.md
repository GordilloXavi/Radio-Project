ssh as root:
`ssh root@134.209.192.226`

# Firewall:
See apps:
`ufw app list`
Add new rule:
`ufw {allow/deny} <app_name>`
Check current rules:
`ufw status`

# Nginx
Check server status:
`systemctl status nginx`
Reload Nginx (to apply config changes):
Check the syntax of the config files first:
`nginx -t`
`systemctl reload nginx`



# Important links:
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04?utm_source=local&utm_medium=Email_Internal&utm_campaign=Email_UbuntuDistroNginxWelcome&mkt_tok=eyJpIjoiTTJFd1pXWmhZamt4TnpRdyIsInQiOiJrYWlpVlRlTWFmUkg5SnZVYmxVUjk0dUEwMXd3YUdrc2N5K08rUlhDT2xPMUIxS1BnZFVlQ3V6dUxNRXQrN2tMbXBJVms2VVNrdlAybmw3c2hNemlaWUFWZ1p3Q24rV2xnNzg2VGM2azFnSm8wcncwQ0xDK09cL2ZkMFA5UzNMdXcifQ%3D%3D

