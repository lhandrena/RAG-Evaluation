import {useState} from "react";
import {v4 as generateUuid} from "uuid";
import {completeChat, type ResponseDto} from "./backend-client.ts";


export interface Message {
    id: string;
    content: string;
    sender: "user" | "bot";
}

export interface SessionState {
    chat_history: Message[];
}

const INITIAL_MESSAGE_1: Message = {
    id: "initial-message-1",
    content: `Hallo, schön dass du da bist.`,
    sender: "bot",
};


export const INITIAL_SESSION_STATE: SessionState = {
    chat_history: [INITIAL_MESSAGE_1],
};

export function userMessage(content: string): Message {
    return {
        id: generateUuid(),
        content,
        sender: "user",
    };
}

export function botMessage(content: string): Message {
    return {
        id: generateUuid(),
        content,
        sender: "bot",
    };
}

export const useChatSessionState = () => {
    const [sessionState, setSessionState] = useState(INITIAL_SESSION_STATE);
    const [waitingForBot, setWaitingForBot] = useState(false);

    async function changeState(updatedState: SessionState) {
        setWaitingForBot(true);
        setSessionState(updatedState);
        completeChat(updatedState)
            .then((answer: ResponseDto) => {
                const stateWithBotMessage = {
                    ...updatedState,
                    chat_history: updatedState.chat_history.concat([
                        botMessage(answer.reply),
                    ]),
                };
                setSessionState(stateWithBotMessage);
                setWaitingForBot(false);
            })
            .catch((error) => {
                console.error("Failed to reach backend:", error);
                const stateWithErrorMessage = {
                    ...updatedState,
                    chat_history: updatedState.chat_history.concat([
                        botMessage("⚠️ Cannot reach backend."),
                    ]),
                };
                setSessionState(stateWithErrorMessage);
                setWaitingForBot(false);
            });
    }


    return {sessionState, changeState, waitingForBot};
};
