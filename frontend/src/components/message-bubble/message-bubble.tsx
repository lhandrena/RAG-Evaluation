import "./message-bubble.css";
import type {Message} from "../../use-session-state.ts";
import ReactMarkdown from 'react-markdown';

interface ChatBubbleProps {
    message: Message;
}

export function MessageBubble({message}: ChatBubbleProps) {
    return (
        <div className={`message ${message.sender === "bot" ? "bot" : "user"}`}>
            <div>
                <ReactMarkdown>
                    {message.content}
                </ReactMarkdown>
            </div>
        </div>
    );
}
