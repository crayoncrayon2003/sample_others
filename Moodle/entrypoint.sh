#!/bin/bash
set -e

DB_HOST="${MOODLE_DB_HOST:-db}"
DB_NAME="${MOODLE_DB_NAME:-moodle}"
DB_USER="${MOODLE_DB_USER:-moodle}"
DB_PASS="${MOODLE_DB_PASSWORD:-moodlepassword}"
WWWROOT="${MOODLE_URL:-http://localhost:8080}"
ADMIN_USER="${MOODLE_ADMIN_USER:-admin}"
ADMIN_PASS="${MOODLE_ADMIN_PASSWORD:-Admin1234!}"
ADMIN_EMAIL="${MOODLE_ADMIN_EMAIL:-admin@example.com}"
SITE_NAME="${MOODLE_SITE_NAME:-My Moodle Site}"

CONFIG_FILE="/var/www/html/config.php"
DATA_DIR="/var/moodledata"
FLAG_FILE="${DATA_DIR}/.installed"

if [ ! -f "$CONFIG_FILE" ]; then
    cat > "$CONFIG_FILE" << EOF
<?php
unset(\$CFG);
global \$CFG;
\$CFG = new stdClass();
\$CFG->dbtype    = 'mariadb';
\$CFG->dblibrary = 'native';
\$CFG->dbhost    = '${DB_HOST}';
\$CFG->dbname    = '${DB_NAME}';
\$CFG->dbuser    = '${DB_USER}';
\$CFG->dbpass    = '${DB_PASS}';
\$CFG->prefix    = 'mdl_';
\$CFG->dboptions = array('dbpersist' => 0, 'dbport' => 3306, 'dbsocket' => '');
\$CFG->wwwroot   = '${WWWROOT}';
\$CFG->dataroot  = '${DATA_DIR}';
\$CFG->admin     = 'admin';
\$CFG->directorypermissions = 0777;
require_once(__DIR__ . '/lib/setup.php');
EOF
    chown www-data:www-data "$CONFIG_FILE"
fi

if [ ! -f "$FLAG_FILE" ]; then
    echo "Waiting for database at ${DB_HOST}..."
    until php -r "
\$m = new mysqli('${DB_HOST}', '${DB_USER}', '${DB_PASS}', '${DB_NAME}');
if (\$m->connect_error) { exit(1); }
exit(0);
" 2>/dev/null; do
        sleep 3
    done
    echo "Database ready. Installing Moodle (this takes a few minutes)..."

    php /var/www/html/admin/cli/install_database.php \
        --agree-license \
        --fullname="${SITE_NAME}" \
        --shortname="moodle" \
        --adminuser="${ADMIN_USER}" \
        --adminpass="${ADMIN_PASS}" \
        --adminemail="${ADMIN_EMAIL}"

    touch "$FLAG_FILE"
    chown www-data:www-data "$FLAG_FILE"
    echo "Moodle installation complete."
fi

exec apache2-foreground
