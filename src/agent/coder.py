class CoderNode:
    def __init__(self, llm):
        self.llm = llm
    def generate_code(self, step, columns):
        if 'visual' in step.lower() or 'chart' in step.lower():
            return 'import matplotlib.pyplot as plt\nplt.figure()\ndf.groupby("Category")["Revenue"].sum().plot(kind="bar")\nplt.title("Revenue by Category")'
        return 'print(df.describe())'
