import gradio as gr
import os
demo = None #added to allow restart

def start_game(main_loop, share=False):
    # added code to support restart
    global demo
    # If demo is already running, close it first
    if demo is not None:
        demo.close()

    demo = gr.ChatInterface(
        main_loop,
        chatbot=gr.Chatbot(height=250, placeholder="Type 'start game' to begin"),
        textbox=gr.Textbox(placeholder="What do you do next?", container=False, scale=7),
        title="AI RPG",
        # description="Ask Yes Man any question",
        theme="soft",
        examples=["Look around", "Continue the story"],
        cache_examples=False,
        retry_btn="Retry",
        undo_btn="Undo",
        clear_btn="Clear",
                           )
    demo.launch(share=share, server_name="0.0.0.0")

def test_main_loop(message, history):
    return 'Entered Action: ' + message

start_game(test_main_loop)