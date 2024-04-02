FROM nginx:1.25.3-alpine-slim

COPY . /usr/share/nginx/html/

EXPOSE 80


##docker build --platform linux/amd64 -t monta010/manual:4.0 .  
##docker run -d -p 8888:80 --name web monta010/manual:2.0



##docker stop web && docker rm web

#docker push monta010/manual:4.0