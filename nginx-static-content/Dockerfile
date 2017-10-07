FROM nginx:1.13.5

ADD index.html /data/www/
ADD duck.jpg /data/images/
ADD ./etc/nginx/nginx.conf /etc/nginx

# note that there's no CMD directive, the existing one
# from the parent container image is preserved. in other
# words, it starts nginx :)
