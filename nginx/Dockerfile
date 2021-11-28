FROM nginx:1.15-alpine

RUN apk add --no-cache nginx-mod-http-lua
RUN mkdir -p /run/nginx
# RUN rm -r /etc/nginx/conf.d && rm /etc/nginx/nginx.conf

CMD ["nginx"]
