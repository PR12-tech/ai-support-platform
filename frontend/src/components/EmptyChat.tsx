type EmptyChatProps = {
    onSelectPrompt: (prompt: string) => void;
};

function EmptyChat({ onSelectPrompt }: EmptyChatProps) {
    const suggestions = [
        {
            icon: "📘",
            label: "What's your refund policy?",
            text: "What is your refund eligibility policy?",
        },
        {
            icon: "📦",
            label: "Can you check my order status?",
            text: "Can you check the status of my order ORD_DEMO1?",
        },
        {
            icon: "🎫",
            label: "Can you check my ticket status?",
            text: "Can you check the status of my ticket TKT1001?",
        },
    ];

    return (
        <div className="flex flex-1 flex-col items-center justify-center bg-slate-50 px-8 py-16 text-center">
            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-indigo-100 text-3xl shadow-inner">
                🤖
            </div>

            <h2 className="mt-6 text-3xl font-bold tracking-tight text-slate-900">
                How can we help you today?
            </h2>

            <p className="mt-2 max-w-md text-sm text-slate-500">
                Ask about order statuses, raise support tickets, verify returns, or search our operational policies.
            </p>

            <div className="mt-10 w-full max-w-lg space-y-3">
                <span className="block text-left text-xs font-semibold uppercase tracking-wider text-slate-400 px-1">
                    Suggested Prompts
                </span>

                <div className="grid gap-3 sm:grid-cols-1">
                    {suggestions.map((item, index) => (
                        <button
                            key={index}
                            onClick={() => onSelectPrompt(item.text)}
                            className="flex items-center gap-3 rounded-xl border border-slate-200 bg-white p-4 text-left text-sm font-medium text-slate-700 shadow-sm transition hover:border-indigo-500 hover:bg-indigo-50/10 focus:outline-none"
                        >
                            <span className="text-xl">{item.icon}</span>
                            <span className="flex-1">{item.label}</span>
                            <span className="text-slate-400 group-hover:text-indigo-600">→</span>
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default EmptyChat;