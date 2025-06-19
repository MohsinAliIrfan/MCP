# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"\nAdding {a} and {b}")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a persona lized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="stdio")

#the stdio means standard input output to recieve and respond to tool function calls
#lets say the server is running somesought of command prompt, the client hit something
#or input some values, the output would be readable by the client/user directly
