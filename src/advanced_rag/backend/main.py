import logging

logging.basicConfig(level=logging.INFO)
logging.info("🚀 Starting backend, loading dependencies (this may take 10-30s)...")

from flask import Flask, request, jsonify
from flask_cors import CORS
from langfuse.langchain import CallbackHandler
from pydantic import ValidationError

from advanced_rag.backend.core.application import Application
from advanced_rag.backend.data_models.conversation_state import ConversationState
from advanced_rag.backend.data_models.response_dto import ResponseDTO



def create_flask_app():
    logging.info("Initializing Langfuse handler...")
    langfuse_handler = CallbackHandler()
    
    logging.info("Initializing application core...")
    app_core = Application(langfuse_handler)
    
    logging.info("Warming up application...")
    _ = app_core.vector_store
    _ = app_core.graph
    logging.info("Application ready!")
    
    app = Flask(__name__)
    CORS(
        app,
        origins=[
            "http://localhost:5173"
        ],
    )

    @app.route(
        '/chat-completion',
        methods=[
            'POST'
        ],
    )
    def chat_completion():
        try:
            data = request.get_json()
            conversation_state = ConversationState(**data)


        except ValidationError as e:
            return jsonify(
                {
                    "error": str(e)
                },
            ), 400

        answer: ResponseDTO = app_core.ask(conversation_state.chat_history)
        return jsonify(answer.model_dump())

    return app


if __name__ == "__main__":
    flask_app = create_flask_app()
    flask_app.run(debug=True, use_debugger=False, use_reloader=False)
