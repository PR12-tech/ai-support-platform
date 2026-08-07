type Message = {
    id: number;
    role: "user" | "assistant";
    content: string;
}

type ChatMessageProps = {
    message: Message;
};

function ChatMessage({ message}: ChatMessageProps) {
    return (
        <div 
        className={`mb-4 flex ${
        message.role === "user" ? "justify-end" : "justify-start"
        }`}
        >
            <div 
            className={`max-w-[70%] rounded-lg px-4 py-3 ${
                message.role === "user"
                ? "bg-blue-600 text-white"
                : "bg-gray-300 text-black"
            }`}
            >
                {message.content}
            </div>
        </div>
    );
}

export default ChatMessage;