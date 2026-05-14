from langgraph.graph import StateGraph, START, END ,MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatMessagePromptTemplate

from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBotNode
import datetime


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
        
    def basic_chatbot_builder_graph(self):
        """
        Builders a basic chatbot graph using Langgraph.
        This method initialized a chatbot node using the 'BasicChatBotNode' class
        and integrates it into the graph. The chatbot node is set as bot the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node=BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
        
        
    def setup_graph(self,usecase:str):
        """sets up the graph for the selected use case."""
        
        if usecase =="Basic Chatbot":
            self.basic_chatbot_builder_graph()
            
        return self.graph_builder.compile()
