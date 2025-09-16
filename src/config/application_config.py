from pydantic import BaseModel


## rest_api
class UvicornConfig(BaseModel):
    host: str
    port: int
    reload: bool


class RestApiConfig(BaseModel):
    title: str
    description: str
    version: str
    docs_url: str
    redoc_url: str
    uvicorn: UvicornConfig


## datasource
class PoolConfig(BaseModel):
    pool_name: str
    min_size: int = 1
    max_size: int = 10


class PostgresConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str
    pool: PoolConfig


class DataSourceConfig(BaseModel):
    postgres: PostgresConfig


class ChatAppConfig(BaseModel):
    rest_api: RestApiConfig
    datasource: DataSourceConfig


## server
class ServerConfig(BaseModel):
    path: str


## chat_application
class ApplicationConfig(BaseModel):
    server: ServerConfig
    chat_application: ChatAppConfig
