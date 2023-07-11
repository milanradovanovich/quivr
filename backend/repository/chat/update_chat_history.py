from typing import List  # For type hinting

from fastapi import HTTPException
from models.chat import ChatHistory
from models.settings import common_dependencies


def update_chat_history(chat_id: str, user_message: str, assistant: str) -> ChatHistory:
    commons = common_dependencies()
    if (
        response := commons["supabase"]
        .table("chat_history")
        .insert(
            {
                "chat_id": chat_id,
                "user_message": user_message,
                "assistant": assistant,
            }
        )
        .execute()
        .data
    ):
        return ChatHistory(response[0])  # pyright: ignore reportPrivateUsage=none
    else:
        raise HTTPException(
            status_code=500, detail="An exception occurred while updating chat history."
        )
