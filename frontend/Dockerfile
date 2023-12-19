# Koristi zvanični Node.js image
FROM node:18-alpine as builder

# Postavi radni direktorijum u /app
WORKDIR /app
COPY package*.json ./
RUN npm install 
# Kopiraj ceo projekat u radni direktorijum
COPY . .
RUN npm run build

FROM nginx
EXPOSE 80
COPY --from=builder /app/build /usr/share/nginx/html
COPY /nginx/nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]