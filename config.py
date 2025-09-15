import yaml
from pydantic import BaseModel

class ServerConfig(BaseModel):
    path: str
    port: int

class Config(BaseModel):
    server: ServerConfig

def load_config(path: str = "application.yml") -> Config:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    return Config(**raw)

settings = load_config()
