from fabric.api import env, local, run, get
import os

env.user = 'bat'
env.hosts = ['rebl.us']

MYSQL_AUTH="-u blog -p'myCleverPassw0rd'"

def get_remote_db():
    run('mkdir -p ~/blog/database')
    run('mysqldump blog %s > ~/blog/database/blog.sql' % MYSQL_AUTH)
    if os.path.exists('database/blog.sql'):
        local('mv database/blog.sql database/blog.sql.bak')
    get('~/blog/database/blog.sql', 'database/blog.sql')

def drop_local_db():
    local('mysqladmin drop blog -f %s' % MYSQL_AUTH)

def load_local_db():
    local('mysqladmin create blog -f %s' % MYSQL_AUTH)
    local('mysql blog %s < database/blog.sql' % MYSQL_AUTH)

def apply_local_settings():
    local('php config_wp_local.php')

def update_local_db():
    get_remote_db()
    drop_local_db()
    load_local_db()
    apply_local_settings()

