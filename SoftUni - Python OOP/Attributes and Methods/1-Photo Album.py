import numpy


class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = numpy.zeros((pages, pages))


