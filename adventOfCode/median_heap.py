class MinHeap():
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)
        self.swap_up(len(self.data))

    def swap_up(self, index):
        if index == 0:
            return
        if self.data[index] < self.data[index // 2]:
            self.data[index], self.data[index // 2] = self.data[index // 2], self.data[index]
            self.swap_up(index // 2)

    def swap_down(self, index):
        if index*2+1 >= len(self.data)-1:
            return

        if index*2+2 >= len(self.data)-1:
            m_child = index*2
        else:
            m_child = index * 2 if self.data[index * 2+1] < self.data[index * 2 + 2] else index * 2 + 1

        if self.data[index] > self.data[m_child]:
            self.data[index], self.data[m_child] = self.data[m_child], self.data[index]
            self.swap_down(m_child)

    def extract_min(self):
        val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.swap_down(0)
