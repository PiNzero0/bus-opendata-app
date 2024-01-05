FROM node:16-alpine
WORKDIR /usr/src/app/frontend
COPY ./frontend /usr/src/app/frontend
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "start"]