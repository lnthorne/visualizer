class MainModel:
    def __init__(self):
        self.left_channel = None
        self.right_channel = None
        self.num_samples = 0
        self.sample_rate = 0

    def load_data(self, left_channel, right_channel, num_samples, sample_rate):
        self.left_channel = left_channel
        self.right_channel = right_channel
        self.num_samples = num_samples
        self.sample_rate = sample_rate

    def get_left_channel(self):
        return self.left_channel

    def get_right_channel(self):
        return self.right_channel

    def get_num_samples(self):
        return self.num_samples

    def get_sample_rate(self):
        return self.sample_rate
