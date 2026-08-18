import ReactMarkdown from "react-markdown";

type Message = {
    id: number;
    role: "user" | "assistant";
    content: string;
};

type ChatMessageProps = {
    message: Message;
};

function ChatMessage({ message }: ChatMessageProps) {
    const isUser = message.role === "user";

    return (
        <div className={`mb-6 flex items-start gap-3 ${isUser ? "justify-end" : "justify-start"}`}>
            
            {/* Robot Avatar for Assistant */}
            {!isUser && (
                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-base shadow-sm border border-slate-200">
                    🤖
                </div>
            )}

            <div
                className={`max-w-[75%] px-4 py-3 shadow-sm ${
                    isUser
                        ? "rounded-2xl rounded-tr-sm bg-indigo-600 text-white"
                        : "rounded-2xl rounded-tl-sm bg-white border border-slate-200 text-slate-800"
                }`}
            >
                {isUser ? (
                    <div className="whitespace-pre-wrap text-sm leading-relaxed">{message.content}</div>
                ) : (
                    <div className="prose prose-slate max-w-none text-sm leading-relaxed">
                        <ReactMarkdown
                            components={{
                                h1: ({ children }) => (
                                    <h1 className="mb-3 mt-2 text-xl font-bold text-slate-900">
                                        {children}
                                    </h1>
                                ),
                                h2: ({ children }) => (
                                    <h2 className="mb-2 mt-4 text-lg font-semibold text-slate-900">
                                        {children}
                                    </h2>
                                ),
                                h3: ({ children }) => (
                                    <h3 className="mb-2 mt-3 text-base font-semibold text-slate-900">
                                        {children}
                                    </h3>
                                ),
                                p: ({ children }) => (
                                    <p className="mb-3 last:mb-0 text-slate-700">
                                        {children}
                                    </p>
                                ),
                                ul: ({ children }) => (
                                    <ul className="mb-3 list-disc space-y-1 pl-5 text-slate-700">
                                        {children}
                                    </ul>
                                ),
                                ol: ({ children }) => (
                                    <ol className="mb-3 list-decimal space-y-1 pl-5 text-slate-700">
                                        {children}
                                    </ol>
                                ),
                                li: ({ children }) => (
                                    <li className="pl-1">
                                        {children}
                                    </li>
                                ),
                                a: ({ children, href }) => (
                                    <a
                                        href={href}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="font-semibold text-indigo-600 underline hover:text-indigo-500"
                                    >
                                        {children}
                                    </a>
                                ),
                                code: ({ children }) => (
                                    <code className="rounded bg-slate-100 px-1.5 py-0.5 font-mono text-xs font-semibold text-slate-900 border border-slate-200">
                                        {children}
                                    </code>
                                ),
                            }}
                        >
                            {message.content}
                        </ReactMarkdown>
                    </div>
                )}
            </div>

            {/* Initials Avatar for User */}
            {isUser && (
                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-indigo-100 font-semibold text-indigo-700 text-xs shadow-sm uppercase">
                    U
                </div>
            )}
        </div>
    );
}

export default ChatMessage;