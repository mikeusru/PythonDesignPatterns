from app.strategy.Compressor import Compressor


class PngCompressor(Compressor):
    def compress(self, file_name):
        print("Compressing using PNG")