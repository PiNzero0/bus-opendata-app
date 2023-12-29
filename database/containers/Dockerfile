# Dockerfile

FROM postgres:16

ENV LANG ja_JP.UTF-8
ENV TZ Asia/Tokyo
RUN apt-get update && apt-get install locales dialog tzdata -y \
               && localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 \
               && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
RUN apt update \
    && apt-get install postgresql-16-postgis-3 -y

