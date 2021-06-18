FROM kong:2.0
LABEL MAINTAINER samngms@gmail.com

USER root

# if you want to install a local rock file, you copy it to the image and then install it
#COPY kong-plugin-request-firewall-0.2.11-1.all.rock /
#RUN luarocks install /kong-plugin-request-firewall-0.2.11-1.all.rock
RUN luarocks install kong-plugin-request-firewall

# if you want to install a local rock file, you copy it to the image and then install it
#COPY kong-plugin-flexible-rate-limit-0.0.15-1.all.rock /
#RUN luarocks install /kong-plugin-flexible-rate-limit-0.0.15-1.all.rock
RUN luarocks install kong-plugin-flexible-rate-limit
