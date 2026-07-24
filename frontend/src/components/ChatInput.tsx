import { useState } from "react";

function ChatInput(){

    const [message, setMessage] = useState("");
    return (
        <form className="flex gap-3">
            <input
            type="text"
            placeholder="Type your message..."
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            className="flex-1 rounded-md border border-gray-300 px-4 py-3 outline-none focus:border-blue-500"
            />

            <button
            type="submit"
            className="rounded-md bg-blue-600 px-6 py-3 font-medium text-white hover:bg-blue-700"
            >
             Send
            </button>
        </form>
    );
}

export default ChatInput;