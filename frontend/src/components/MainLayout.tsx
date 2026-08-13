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
};

function MainLayout ({ 
    conversations,
    selectedConversation, 
    onNewChat,
    onConversationSelect,
    onConversationDelete,
    isCreatingConversation,
    deletingConversationId, 
}: MainLayoutProps) {
    
    return (
        <main className="flex min-h-0 flex-1 overflow-hidden">
            <Sidebar 
            conversations={conversations}
            selectedConversation={selectedConversation} 
            onNewChat={onNewChat} 
            onConversationSelect={onConversationSelect}
            onConversationDelete={onConversationDelete}
            isCreatingConversation={isCreatingConversation}
            deletingConversationId={deletingConversationId} 
            />

            {
                selectedConversation && (
                    <ChatWorkSpace
                    selectedConversation={selectedConversation} 
                    />
                )}
        </main>
    );
}

export default MainLayout;