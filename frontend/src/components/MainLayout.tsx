import Sidebar from "./Sidebar";
import ChatWorkSpace from "./ChatWorkSpace";
import type { Conversation } from "../types/conversation";


type MainLayoutProps = {
    conversations: Conversation[];
    selectedConversation: Conversation;
    onNewChat: () => void;
    onConversationSelect: (conversation: Conversation) => void;
};

function MainLayout ({ 
    conversations,
    selectedConversation, 
    onNewChat,
    onConversationSelect, 
}: MainLayoutProps) {
    
    return (
        <main className="flex flex-1 overflow-hidden">
            <Sidebar 
            conversations={conversations}
            selectedConversation={selectedConversation} 
            onNewChat={onNewChat} 
            onConversationSelect={onConversationSelect} 
            />
            <ChatWorkSpace
            selectedConversation={selectedConversation} 
            />
        </main>
    );
}

export default MainLayout;