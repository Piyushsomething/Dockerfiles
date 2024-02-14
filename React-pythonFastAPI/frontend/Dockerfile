# Use the official Nginx image as a base image
FROM nginx:alpine

# Copy the built React app from your local machine to the container
COPY frontend/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
