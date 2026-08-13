import ReactMarkdown from "react-markdown";

type Message = {
    id: number;
    role: "user" | "assistant";
    content: string;
}

type ChatMessageProps = {
    message: Message;
};

function ChatMessage({ message }: ChatMessageProps) {
    return (
        <div
            className={`mb-4 flex ${message.role === "user" ? "justify-end" : "justify-start"
                }`}
        >
            <div
                className={`max-w-[70%] rounded-lg px-4 py-3 ${message.role === "user"
                        ? "bg-blue-600 text-white"
                        : "bg-gray-300 text-black"
                    }`}
            >
                {message.role === "assistant" ? (
                    <ReactMarkdown
                        components={{
                            h1: ({ children }) => (
                                <h1 className="mb-3 mt-2 text-2xl font-bold">
                                    {children}
                                </h1>
                            ),

                            h2: ({ children }) => (
                                <h2 className="mb-2 mt-4 text-xl font-semibold">
                                    {children}
                                </h2>
                            ),

                            h3: ({ children }) => (
                                <h3 className="mb-2 mt-3 text-lg font-semibold">
                                    {children}
                                </h3>
                            ),

                            p: ({ children }) => (
                                <p className="mb-3 last:mb-0">
                                    {children}
                                </p>
                            ),

                            ul: ({ children }) => (
                                <ul className="mb-3 list-disc space-y-1 pl-6">
                                    {children}
                                </ul>
                            ),

                            ol: ({ children }) => (
                                <ol className="mb-3 list-decimal space-y-1 pl-6">
                                    {children}
                                </ol>
                            ),

                            li: ({ children }) => (
                                <li>
                                    {children}
                                </li>
                            ),

                            a: ({ children, href }) => (
                                <a
                                    href={href}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="underline"
                                >
                                    {children}
                                </a>
                            ),

                            code: ({ children }) => (
                                <code className="rounded bg-gray-200 px-1.5 py-0.5 font-mono text-sm">
                                    {children}
                                </code>
                            ),
                        }}
                    >
                        {message.content}
                    </ReactMarkdown>
                ) : (
                    message.content
                )}
            </div>
        </div>
    );
}

export default ChatMessage;