#this client must be able to interact with matherserver and weatherserve

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio
import os
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# lets initialize the tools
async def main():

    print("\n Main agent called")

    client = MultiServerMCPClient(
        {
            #math is going to be one of the server
            "math": {
                "command": "python", #used to execute the mathserver.py file
                "args": ["mathserver.py"], #because math server is not in any other directory but just paralell to the 
                "transport": "stdio" #this is the transport that is used to communicate with the math server
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            }
        }
    ) 

    print("\n Getting the tools")
    tool = await client.get_tools()
    # print(tool)

    #lets get the model
    model = ChatGroq(
        model="qwen-qwq-32b",
    )

    agent = create_react_agent(
        model=model,
        tools=tool,
    )
    
    print("\n invoking the agent")
    maths_response = await agent.ainvoke(
        {"messages" : [{"role": "user", "content": "What is 10 + 10?"}]}
    )
    print(maths_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages" : [{"role": "user", "content": "what is the temprature in Lahore"}]}
    )
    print(weather_response["messages"][-1].content)
    

# To run the async main function
if __name__ == "__main__":
    asyncio.run(main())



