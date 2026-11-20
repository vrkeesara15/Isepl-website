FROM caddy:2.8-alpine
COPY Caddyfile /etc/caddy/Caddyfile
COPY site /srv
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
