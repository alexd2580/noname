cd "$(dirname "$0")"
make venv
source local_env.sh
flask run -h 0.0.0.0 -p 8080 --with-threads
