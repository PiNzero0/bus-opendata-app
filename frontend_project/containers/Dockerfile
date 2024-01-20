FROM node:16-alpine
WORKDIR /usr/src/app/frontend 
COPY ./frontend /usr/src/app/frontend
RUN npm install

RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache
EXPOSE 3000
CMD ["npm", "run", "start"]