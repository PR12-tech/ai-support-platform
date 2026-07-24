function EmptyChat() {
    return (
        <div className="flex flex-1 flex-col items-center justufy-center px-8 text-center">
            <div className="mb-6 text-6xl">
            🤖
            </div>

            <h2 className="mb-4 text-3xl font-semibold">
                AI Customer Support Assistant
            </h2>

            <p className="mb-8 max-w-xl text-gray-500">
                Ask question about orders, tickets, analytics, or company
                knowledge. I will use the appropriate tools to help you.
            </p>

            <div className="space-y-3 text-left">
                <p>✅ Order Tracking</p>
                <p>✅ Ticket Lookup</p>
                <p>✅ SQL Analytics</p>
                <p>✅ Knowledge Base Search</p>
            </div>
        </div>
    );
}

export default EmptyChat;