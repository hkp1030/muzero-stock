class Environment:
    PRICE_IDX = 4  # 종가의 위치

    def __init__(self, chart_data=None, training_data=None):
        self.chart_data = chart_data
        self.training_data = training_data
        self.observation = None
        self.idx = 0
        self.done = False

    def reset(self):
        self.observation = None
        self.idx = 0
        self.done = False

    def observe(self):
        if self.done:
            return None

        self.idx += 1
        self.observation = self.training_data.iloc[self.idx]

        if len(self.chart_data) >= self.idx + 1:
            self.done = True

        return self.observation, self.done

    def get_price(self):
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None
