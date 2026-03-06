"""Stub for a Claude-like multi-agent orchestrator."""
from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def act(self, observation):
        pass


class ClaudeAgent:
    def __init__(self, agents):
        self.agents = agents

    def run(self, initial_input):
        obs = initial_input
        for agent in self.agents:
            obs = agent.act(obs)
        return obs


# example concrete agents
class SalesAnalyzer(Agent):
    def act(self, observation):
        # run some analysis or call RAG etc.
        from agents.rag import RAG
        rag = RAG()
        answer = rag.ask(observation)
        return answer