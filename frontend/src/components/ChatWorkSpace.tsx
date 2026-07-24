import EmptyChat from "./EmptyChat";
import ChatInput from "./ChatInput";

function ChatWorkSpace() {
    return (
        <section className="flex flex-1 flex-col bg-white">
            <header className="border-b px-6 py-4">
                <h2 className="text-xl font-semibold">
                    AI Customer Support Assistant
                </h2>
            </header>


            <main className="flex flex-1">
                <EmptyChat />
            </main>


            <footer className="border-t p-4">
                <ChatInput />
            </footer>
        </section>
    );
}

export default ChatWorkSpace