import asyncio
from agents import Agent, Runner
from mcp.server.fastmcp import FastMCP

app = FastMCP("rackgen-mcp")

rackgen_agent = Agent(
    name="RackGen",
    instructions=(
        "Genera módulos para VCV Rack en C++: estructura de plugin, CMake, "
        "manifest y DSP mínimo. Devuelve 'archivos' con rutas y contenido."
    )
)

@app.tool()
async def generate(prompt: str) -> dict:
    """
    Genera un módulo VCV Rack a partir de un prompt.
    Retorna un objeto con archivos {ruta: contenido} y notas.
    """
    run = await Runner.run(rackgen_agent, prompt)
    return {
        "notes": "Salida textual del agente (formatea a archivos en el cliente):",
        "raw_output": run.final_output,
    }

if __name__ == "__main__":
    app.run()
