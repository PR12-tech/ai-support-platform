import { useState } from "react";
import EmptyChat from "./EmptyChat";
import ChatInput from "./ChatInput";
import MessageList from "./MessageList";
import TypingIndicator from "./TypingIndicator";
import { askQuestion } from "../services/ChatService";

function ChatWorkSpace() {

    type Message = {
        id: number;
        role: "user" | "assistant";
        content: string;
};
    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const sessionId = "demo-session";

    async function handleSendMessage(message: string) {

        setMessages((previousMessages) => [
            ...previousMessages,
            {
                id: Date.now(),
                role: "user",
                content: message,
            },
        ]);

        setIsLoading(true);

        try {

            const response = await askQuestion({
                session_id: sessionId,
                question: message,
            });

            setMessages((previousMessages) => [
                ...previousMessages,
                {
                    id: Date.now() + 1,
                    role: "assistant",
                    content: response.answer,
                },
            ]);

        } catch (error) {

            console.error(error);

            setMessages((previousMessages) => [
                ...previousMessages,
                {
                    id: Date.now() + 1,
                    role: "assistant",
                    content: "Unable to reach the backend.",
                },
            ]);

        } finally {

            setIsLoading(false);

        }
    }

    return (
        <section className="flex flex-1 flex-col bg-white">
            <header className="border-b px-6 py-4">
                <h2 className="text-xl font-semibold">
                    AI Customer Support Assistant
                </h2>
            </header>


            <main className="flex flex-1 flex-col overflow-hidden">
                {messages.length === 0 ? (
                <EmptyChat />
            ) : (

                <div className="flex flex-1 flex-col overflow-hidden">
                    
                    <MessageList messages={messages} />

                    {isLoading && <TypingIndicator />}
                    
                    </div>
                )}
            </main>


            <footer className="border-t p-4">
                <ChatInput
                onSendMessage={handleSendMessage}
                isLoading={isLoading}
                />
            </footer>
        </section>
    );
}

export default ChatWorkSpace