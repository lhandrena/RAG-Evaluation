import axios from "axios";
import type {SessionState} from "./use-session-state.ts";


const BACKEND_BASE_PATH = import.meta.env.VITE_BACKEND_BASE_PATH;
const CHAT_COMPLETION_PATH: string = BACKEND_BASE_PATH + "/chat-completion";

export interface ResponseDto {
    reply: string;
}

export async function completeChat(
    sessionState: SessionState,
): Promise<ResponseDto> {
    const {data: response} = await axios
        .post(CHAT_COMPLETION_PATH, sessionState, {
            headers: {"Content-Type": "application/json"},
        }).catch((error => {
            console.error("Error while calling backend:", error);
            throw error;
        }));
    return response;
}