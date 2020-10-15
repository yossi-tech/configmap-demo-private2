from multiprocessing import cpu_count
import os 

workers = os.getenv('WEB_CONCURRENCY',cpu_count()*2)
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "5001")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

loglevel = use_loglevel
bind = use_bind
# worker_class = "gthread"
# threads = 2 
