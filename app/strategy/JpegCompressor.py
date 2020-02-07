from app.strategy.Compressor import Compressor


class JpegCompressor(Compressor):
    def compress(self, file_name):
        print("Compressing using JPEG")