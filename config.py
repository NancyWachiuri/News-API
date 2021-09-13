
class Config:

   # NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_KEY = ('f4c86580284a4e12bd792c731cfe34c4')
    SECRET_KEY = ('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
