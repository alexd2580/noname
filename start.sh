cd "$(dirname "$0")"
make venv
source local_env.sh
uwsgi uwsgi.ini
