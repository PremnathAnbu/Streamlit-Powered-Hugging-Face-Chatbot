import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groq_llm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langraph_agenticai_app():
    """Loads and runs the langgraph agenticai application with streamlist UI.
    This function initialized the ui, handles user input, configures the llm model,
    ests up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness."""
    
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error:Failed to load user input from the UI.")
        return 
    
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    elif st.session_state.IsSDLC:
        user_message=st.session_state.state
    else:
        user_message=st.chat_input("Enter your message:")
        
    if user_message:
        try:
            obj_llm_config=GroqLLM(user_control_input=user_input)
            model=obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initialized")
                return 
            usecase=user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected")
                return 
            
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
        except Exception as e:
            raise ValueError(f"Error occurred with Exception :{e}")

