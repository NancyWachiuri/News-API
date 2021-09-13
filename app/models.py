class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,source_name,title,author,description, url, poster,date):
        self.id =source_name
        self.news_title = title
        self.overview = author
        self.news_description = description
        self.link = url
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.date = date
        
