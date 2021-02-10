FROM kong:2.0
LABEL MAINTAINER samngms@gmail.com

USER root
RUN luarocks install kong-plugin-request-firewall
RUN luarocks install kong-plugin-flexible-rate-limit