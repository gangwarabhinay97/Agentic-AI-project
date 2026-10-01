class PlannerNode:
    def __init__(self, llm):
        self.llm = llm
    def plan(self, schema, query):
        return ['Compute summary metrics and aggregations', 'Generate category visualization']
