class ImageStorage:
    def __init__(self, compressor, image_filter):
        self.compressor = compressor
        self.filter = image_filter

    def store(self, file_name):
        self.compressor.compress(file_name)
        self.filter.apply(file_name)