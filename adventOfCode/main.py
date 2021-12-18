# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Grid():
    def __init__(self, m, n, default=None):
        self.data = [[default for j in range(n)] for i in range(m)]

    def update(self,m,n,value):
        self.data[m][n] = value

    def get(self,m,n,value):
        if m<0 or n<0 or m>=len(self.data) or n>=len(self.data[0]):
            return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
