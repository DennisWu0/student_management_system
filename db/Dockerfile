# Use official MySQL image as base
FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_HOST=db
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=student_db

# Copy initialization script
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3307

