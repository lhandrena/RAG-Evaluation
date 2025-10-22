import {useState} from "react";
import "./chat-input.css";

interface ChatInputProps {
    addMessage: (messageContent: string) => Promise<void>;
}

export function ChatInput({addMessage}: ChatInputProps) {
    const [inputValue, setInputValue] = useState("");

    const handleSubmit = () => {
        const convertedInput = inputValue.trim();
        if (convertedInput) {
            addMessage(convertedInput);
            setInputValue("");
            document.getElementById("text-input")?.focus();
        }

    };

    const handleKeyDown = (event: React.KeyboardEvent) => {
        if (event.key === "Enter") {
            event.preventDefault();
            handleSubmit();
        }
    };

    return (
        <div className="chat-input">
            <div className="chat-input-row">
                <input
                    id="text-input"
                    className="text-input"
                    autoFocus
                    placeholder="Bitte Text eingeben..."
                    value={inputValue}
                    onChange={(event) => setInputValue(event.target.value)}
                    onKeyDown={handleKeyDown}/>
                <button className="send-button" onClick={handleSubmit}>Senden</button>
            </div>
        </div>
    );
}
