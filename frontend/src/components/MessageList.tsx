import { useEffect, useRef } from "react";
import ChatMessage from "./ChatMessage";

type Message = {
    id: number;
    role: "user" | "assistant";
    content: string;
};

type MessageListProps = {
    messages: Message[];
};

function MessageList({ messages }: MessageListProps) {

    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages]);

    return (
        <div className="min-h-0 flex-1 overflow-y-auto p-6">
            {messages.map((message) => (
                <ChatMessage
                key={message.id}
                message={message}
                />
            ))}
            <div ref={bottomRef}></div>
        </div>

    );
}

export default MessageList;