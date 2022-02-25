class Environment:
    PRICE_IDX = 4  # 종가의 위치

    def __init__(self, chart_data=None, training_data=None):
        self.chart_data = chart_data
        self.training_data = training_data
        self.observation = None
        self.idx = -1

    def reset(self):
        self.observation = None
        self.idx = -1

    def is_done(self):
        if self.idx + 1 >= len(self.training_data):
            return True
        else:
            return False

    def observe(self):
        if self.is_done():
            return None

        self.idx += 1
        self.observation = self.training_data.iloc[self.idx]
        return self.observation.tolist()

    def get_price(self):
        return self.chart_data.iloc[self.idx][self.PRICE_IDX]
