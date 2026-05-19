FROM php:8.2-apache

RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libicu-dev \
    libxml2-dev \
    libzip-dev \
    libonig-dev \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) \
        gd intl mysqli pdo_mysql soap xml zip opcache mbstring exif

RUN a2enmod rewrite && \
    sed -i 's|<Directory /var/www/>|<Directory /var/www/html>|g' /etc/apache2/apache2.conf && \
    printf '\n<Directory /var/www/html>\n    AllowOverride All\n</Directory>\n' \
        >> /etc/apache2/apache2.conf

RUN printf 'max_input_vars=5000\npost_max_size=50M\nupload_max_filesize=50M\nmemory_limit=256M\n' \
    > /usr/local/etc/php/conf.d/moodle.ini

RUN curl -fsSL https://download.moodle.org/download.php/direct/stable405/moodle-latest-405.tgz \
    | tar -xz --strip-components=1 -C /var/www/html && \
    mkdir -p /var/moodledata && \
    chown -R www-data:www-data /var/www/html /var/moodledata && \
    chmod -R 755 /var/www/html

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
