import type { Conversation } from "../types/conversation";

type SidebarProps = {
    conversations: Conversation[];
    selectedConversation: Conversation;
    onNewChat: () => void;
    onConversationSelect: (conversation: Conversation) => void;
};

function Sidebar({ 
    conversations,
    selectedConversation, 
    onNewChat,
    onConversationSelect
}: SidebarProps) {

    return (
        <aside className="w-72 border-r p-4">
            <button 
            onClick={onNewChat}
            className="mb-6 w-full rounded-md bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700">
                + New Chat
            </button> 

            <h2 className="mb-4 text-lg font-semibold">
                Conversation History
            </h2>

            <div className="space-y-2">
                {conversations.map((conversation) => (
                    <div
                    key={conversation.id}
                    onClick={() => onConversationSelect(conversation)}
                    className={
                        conversation.id === selectedConversation.id
                        ? "cursor-pointer rounded-md bg-blue-100 p-2 font-medium text-blue-700"
                        : "cursor-pointer rounded-md p-2 hover:bg-gray-200"
                    }
                >
                    {conversation.title}
                    </div>
                ))}
            </div>
        </aside>
    );
}

export default Sidebar;