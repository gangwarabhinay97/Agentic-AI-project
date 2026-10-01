from typing import TypedDict, List, Dict, Any
class AgentState(TypedDict):
    user_query: str
    plan_steps: List[str]
    logs: List[Dict[str, Any]]
    final_report: str
