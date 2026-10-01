from src.sandbox import SandboxExecutor
from src.agent.planner import PlannerNode
from src.agent.coder import CoderNode
from src.agent.reporter import ReporterNode
class AnalysisAgentWorkflow:
    def __init__(self):
        self.planner = PlannerNode(None); self.coder = CoderNode(None); self.reporter = ReporterNode(None)
    def run(self, df, schema, query, cb=None):
        steps = self.planner.plan(schema, query)
        logs, figs = [], []
        for step in steps:
            code = self.coder.generate_code(step, schema['columns'])
            res = SandboxExecutor.execute(code, df)
            if res['figures']: figs.extend(res['figures'])
            logs.append({'step': step, 'code': code, 'output': res['output']})
        report = self.reporter.generate_report(query, logs)
        return {'steps': steps, 'logs': logs, 'figures': figs, 'report': report}
