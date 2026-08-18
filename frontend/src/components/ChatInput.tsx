import { useState } from "react";

type ChatInputProps = {
    onSendMessage: (message: string) => void;
    isLoading: boolean;
};

function ChatInput({ onSendMessage, isLoading }: ChatInputProps) {
    const [message, setMessage] = useState("");

    function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        if (!message.trim()) return;

        onSendMessage(message.trim());
        setMessage("");
    }

    return (
        <form onSubmit={handleSubmit} className="relative flex items-center">
            <input
                type="text"
                placeholder="Ask support about orders, policies, or tickets..."
                value={message}
                onChange={(event) => setMessage(event.target.value)}
                disabled={isLoading}
                className="w-full rounded-xl border border-slate-300 bg-white py-3.5 pl-4 pr-16 text-sm placeholder-slate-400 shadow-sm outline-none transition focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100 disabled:cursor-not-allowed disabled:bg-slate-50"
            />

            <button
                type="submit"
                disabled={isLoading || !message.trim()}
                className="absolute right-2 rounded-lg bg-indigo-600 p-2 text-white shadow-sm transition hover:bg-indigo-500 disabled:cursor-not-allowed disabled:opacity-40"
                aria-label="Send message"
            >
                {isLoading ? (
                    <svg className="h-4.5 w-4.5 animate-spin" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                ) : (
                    <svg className="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                    </svg>
                )}
            </button>
        </form>
    );
}

export default ChatInput;