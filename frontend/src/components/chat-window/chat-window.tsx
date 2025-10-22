import * as React from "react";
import {useEffect} from "react";
import "./chat-window.css";
import type {Message} from "../../use-session-state.ts";
import {MessageBubble} from "../message-bubble/message-bubble.tsx";
import Spinner from "../spinner/spinner.tsx";


interface ChatWindowProps {
    messages: Message[];
    waitingForBot: boolean;
}

export function ChatWindow({messages, waitingForBot}: ChatWindowProps) {
    const chatWindow = React.createRef<HTMLDivElement>();

    useEffect(() => {
        chatWindow.current!.scrollTop = chatWindow.current!.scrollHeight;
    }, [messages, chatWindow]);

    return (
        <div ref={chatWindow} className="chat-window">
            {messages.map((message) => (
                <MessageBubble key={message.id} message={message}/>
            ))}
            {waitingForBot && (
                <div>
                    <Spinner/>
                </div>
            )}
        </div>
    );
}
