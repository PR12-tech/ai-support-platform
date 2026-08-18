import Sidebar from "./Sidebar";
import ChatWorkSpace from "./ChatWorkSpace";
import type { Conversation } from "../types/conversation";

type MainLayoutProps = {
    conversations: Conversation[];
    selectedConversation: Conversation | null;
    onNewChat: () => void;
    onConversationSelect: (conversation: Conversation) => void;
    onConversationDelete: (conversation: Conversation) => void;
    isCreatingConversation: boolean;
    deletingConversationId: string | null;
    isMobileSidebarOpen?: boolean;
    onCloseMobileSidebar?: () => void;
};

function MainLayout({
    conversations,
    selectedConversation,
    onNewChat,
    onConversationSelect,
    onConversationDelete,
    isCreatingConversation,
    deletingConversationId,
    isMobileSidebarOpen,
    onCloseMobileSidebar,
}: MainLayoutProps) {
    return (
        <main className="flex min-h-0 flex-1 overflow-hidden relative">
            <Sidebar
                conversations={conversations}
                selectedConversation={selectedConversation}
                onNewChat={onNewChat}
                onConversationSelect={onConversationSelect}
                onConversationDelete={onConversationDelete}
                isCreatingConversation={isCreatingConversation}
                deletingConversationId={deletingConversationId}
                isMobileOpen={isMobileSidebarOpen}
                onCloseMobile={onCloseMobileSidebar}
            />

            {selectedConversation ? (
                <ChatWorkSpace selectedConversation={selectedConversation} />
            ) : (
                <div className="flex flex-1 flex-col items-center justify-center bg-slate-50 p-8 text-center">
                    <span className="text-5xl mb-4">🤖</span>
                    <h2 className="text-xl font-bold text-slate-800">Welcome to NovaCart Support</h2>
                    <p className="mt-1.5 text-sm text-slate-500 max-w-sm">
                        Select a conversation from the sidebar or click "+ New Conversation" to start a new support session.
                    </p>
                </div>
            )}
        </main>
    );
}

export default MainLayout;