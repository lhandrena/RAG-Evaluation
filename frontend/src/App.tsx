import './App.css';
import Header from "./components/header/header.tsx";
import {ChatWindow} from "./components/chat-window/chat-window.tsx";
import {useChatSessionState, userMessage} from "./use-session-state.ts";
import {ChatInput} from "./components/chat-input/chat-input.tsx";

function App() {
    const {sessionState, changeState, waitingForBot} = useChatSessionState();

    async function addMessage(messageContent: string) {
        const stateWithUserMessage = {
            ...sessionState,
            chat_history: sessionState.chat_history.concat([
                userMessage(messageContent),
            ]),
        };
        await changeState(stateWithUserMessage);
    }


    return (
        <div className="main-panel">
            <div className="app">
                <Header/>
                <ChatWindow messages={sessionState.chat_history} waitingForBot={waitingForBot}/>
                <ChatInput addMessage={addMessage}/>
            </div>
        </div>
    )
}

export default App
