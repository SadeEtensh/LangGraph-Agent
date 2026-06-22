from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, AIMessage

# 1. Define State (here we use the built-in MessagesState)
# You can also create custom TypedDicts
state = MessagesState

# 2. Define a node (a function that takes state and returns updates)
def chatbot(state: MessagesState):
    # In real apps, call an LLM here
    return {"messages": [AIMessage(content="Hello! How can I help you?")]}

# 3. Build the graph
graph_builder = StateGraph(MessagesState)

graph_builder.add_node("chatbot", chatbot)

# Add edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile
graph = graph_builder.compile()

# Run it
result = graph.invoke({"messages": [HumanMessage(content="Hi!")]})
print(result["messages"][-1].content)