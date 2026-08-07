import { useState } from "react";

type ChatInputProps = {
    onSendMessage: (message: string) => void;
    isLoading: boolean;
};

function ChatInput({
    onSendMessage,
    isLoading,
 }: ChatInputProps) {

    const [message, setMessage] = useState("");

    function handleSubmit(event: React.SyntheticEvent<HTMLFormElement>) {

        event.preventDefault();

        onSendMessage(message)

        setMessage("");
    }
    
    return (
        <form 
        onSubmit={handleSubmit}
        className="flex gap-3">
            <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            disabled={isLoading}
            className="flex-1 rounded-md border border-gray-300 px-4 py-3 outline-none focus:border-blue-500"
            />

            <button
            type="submit"
            disabled={isLoading}
            className="rounded-md bg-blue-600 px-6 py-3 font-medium text-white hover:bg-blue-700"
            >
             Send
            </button>
        </form>
    );
}

export default ChatInput;