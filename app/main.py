import gradio as gr
from components.datalake_ui import datalake_ui
from utils.db import database
import asyncio

def main():
    """
    Main entry point for the VitalEdge Troll app.
    """

    async def initialize_database():
        print("Initializing database connection...")
        await database.connect()
        print("Database connected.")

    async def disconnect_database():
        print("Disconnecting database...")
        await database.disconnect()
        print("Database disconnected.")

    with gr.Blocks() as demo:
        gr.Markdown("# VitalEdge Troll: Experimental System UI")
        
        with gr.Tab("Datalake Explorer"):
            datalake_ui()

        # Initialize the database when the app starts
        asyncio.run(initialize_database())

        # Use the unload event for resource cleanup
        @demo.unload
        async def on_unload():
            await disconnect_database()

        # Launch the app
        demo.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
