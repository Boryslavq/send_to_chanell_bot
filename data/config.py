from environs import Env

env = Env()
env.read_env()

ip = env.str("ip")

PG_USER = env.str("PG_USER")
token = env.str("token")
PG_PASSWORD = env.str("PG_PASSWORD")
PG_NAME = env.str("PG_NAME")

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{ip}/{PG_NAME}"
