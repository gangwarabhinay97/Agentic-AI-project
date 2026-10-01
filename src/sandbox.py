import sys, io, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
class SandboxExecutor:
    @staticmethod
    def execute(code, df):
        old = sys.stdout; sys.stdout = out = io.StringIO(); plt.close('all')
        loc = {'df': df.copy(), 'pd': pd, 'plt': plt}
        ok = True; err = None
        try: exec(code, globals(), loc)
        except Exception as e: ok = False; err = str(e)
        finally: sys.stdout = old
        figs = [plt.figure(n) for n in plt.get_fignums()]
        return {'success': ok, 'output': out.getvalue(), 'error': err, 'figures': figs, 'df': loc.get('df', df)}
