from app.strategy.Filter import Filter


class BlackAndWhiteFilter(Filter):
    def apply(self, file_name):
        print("Applying Black And White Filter")
