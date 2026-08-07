import { useEffect, useState } from "react";
import EmptyChat from "./EmptyChat";
import ChatInput from "./ChatInput";
import MessageList from "./MessageList";
import TypingIndicator from "./TypingIndicator";
import { askQuestion, getHistory } from "../services/ChatService";
import type { Conversation } from "../types/conversation";
import type { Message } from "../types/message";
import type { HistoryMessage } from "../types/api";

type ChatWorkSpaceProps = {
    selectedConversation: Conversation;
};

function ChatWorkSpace({
    selectedConversation,
}: ChatWorkSpaceProps) {

    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const sessionId = selectedConversation.id;

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

    async function loadHistory() {

        try {

            const response = await getHistory(sessionId);

            setMessages(
                response.history.map(
                    (
                        message: HistoryMessage,
                        index: number
                    ) => ({
                        id: index,
                        role: message.role,
                        content: message.content,
                    })
                )
            );
        } catch (error) {

            console.error(error);

        }

    }

    useEffect(() => {

            loadHistory();

    }, [sessionId]);

    return (
        <section className="flex flex-1 flex-col bg-white">
            <header className="border-b px-6 py-4">
                <h2 className="text-xl font-semibold">
                    {selectedConversation.title}
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