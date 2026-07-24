import Sidebar from "./Sidebar";
import ChatWorkSpace from "./ChatWorkSpace";


type MainLayoutProps = {
    conversations: string[];
    selectedConversation: string;
    onNewChat: () => void;
    onConversationSelect: (conversation: string) => void;
};

function MainLayout ({ 
    conversations,
    selectedConversation, 
    onNewChat,
    onConversationSelect, 
}: MainLayoutProps) {
    
    return (
        <main className="flex flex-1">
            <Sidebar 
            conversations={conversations}
            selectedConversation={selectedConversation} 
            onNewChat={onNewChat} 
            onConversationSelect={onConversationSelect} 
            />
            <ChatWorkSpace />
        </main>
    );
}

export default MainLayout;