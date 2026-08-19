import { useEffect, useState, useCallback } from "react";
import EmptyChat from "./EmptyChat";
import ChatInput from "./ChatInput";
import MessageList from "./MessageList";
import TypingIndicator from "./TypingIndicator";
import { getErrorMessage } from "../services/errorHandler";
import { askQuestion, getHistory } from "../services/ChatService";
import type { Conversation } from "../types/conversation";
import type { Message } from "../types/message";
import type { HistoryMessage } from "../types/api";

type ChatWorkSpaceProps = {
    selectedConversation: Conversation;
};

function ChatWorkSpace({ selectedConversation }: ChatWorkSpaceProps) {
    const [isLoading, setIsLoading] = useState(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
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
                    content: getErrorMessage(error),
                },
            ]);
        } finally {
            setIsLoading(false);
        }
    }

    const loadHistory = useCallback(async () => {
        try {
            setErrorMessage(null);
            const response = await getHistory(sessionId);

            setMessages(
                response.history.map((message: HistoryMessage, index: number) => ({
                    id: index,
                    role: message.role,
                    content: message.content,
                }))
            );
        } catch (error) {
            console.error(error);
            setErrorMessage(getErrorMessage(error));
        }
    }, [sessionId]);

    useEffect(() => {
        loadHistory();
    }, [loadHistory]);

    return (
        <section className="flex flex-1 flex-col bg-slate-50 min-w-0">
            {/* Conversation Header */}
            <header className="flex h-16 items-center justify-between border-b border-slate-200 bg-white px-6 shadow-sm">
                <div className="flex items-center gap-3 overflow-hidden">
                    {/* Active Chat Dot Indicator */}
                    <span className="relative flex h-2.5 w-2.5 shrink-0">
                        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"></span>
                        <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-green-500"></span>
                    </span>

                    <h2 className="overflow-hidden text-ellipsis whitespace-nowrap text-base font-bold text-slate-800">
                        {selectedConversation.title}
                    </h2>
                </div>
            </header>

            {/* Chat Messages */}
            <main className="flex flex-1 flex-col overflow-hidden relative">
                {errorMessage && (
                    <div className="mx-6 mt-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800">
                        <div className="flex justify-between items-center">
                            <div className="flex gap-2">
                                <span>⚠️</span>
                                <span>{errorMessage}</span>
                            </div>
                            <button
                                onClick={() => setErrorMessage(null)}
                                className="text-red-500 hover:text-red-700 font-bold"
                            >
                                ✕
                            </button>
                        </div>
                    </div>
                )}

                {messages.length === 0 ? (
                    <div className="min-h-0 flex-1 overflow-y-auto">
                        <EmptyChat onSelectPrompt={handleSendMessage} />
                    </div>
                ) : (
                    <div className="flex flex-1 flex-col overflow-hidden bg-slate-50">
                        <MessageList messages={messages} />
                        {isLoading && (
                            <div className="px-6 py-2">
                                <TypingIndicator />
                            </div>
                        )}
                    </div>
                )}
            </main>

            {/* Input Bar */}
            <footer className="border-t border-slate-200 bg-white p-4 shadow-sm">
                <div className="mx-auto max-w-4xl">
                    <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
                </div>
            </footer>
        </section >
    );
}

export default ChatWorkSpace;