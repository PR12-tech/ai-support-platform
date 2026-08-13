import type { Conversation } from "../types/conversation";

type SidebarProps = {
    conversations: Conversation[];
    selectedConversation: Conversation | null;
    onNewChat: () => void;
    onConversationSelect: (conversation: Conversation) => void;
    onConversationDelete: (conversation: Conversation) => void;
    isCreatingConversation: boolean;
    deletingConversationId: string | null;
};

function Sidebar({
    conversations,
    selectedConversation,
    onNewChat,
    onConversationSelect,
    onConversationDelete,
    isCreatingConversation,
    deletingConversationId,
}: SidebarProps) {

    return (
        <aside className="flex h-full w-72 flex-col border-r p-4">

            <button
                onClick={onNewChat}
                disabled={isCreatingConversation}
                className="mb-6 w-full rounded-md bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
            >

                {isCreatingConversation ? "Creating..." : "+ New Chat"}

            </button>

            <h2 className="mb-4 text-lg font-semibold">
                Conversation History
            </h2>

            <div className="flex-1 space-y-2 overflow-y-auto">
                {conversations.map((conversation) => (
                    <div
                        key={conversation.id}
                        onClick={() => onConversationSelect(conversation)}
                        className={
                            conversation.id === selectedConversation?.id
                                ? "cursor-pointer rounded-md bg-blue-100 p-2 font-medium text-blue-700"
                                : "cursor-pointer rounded-md p-2 hover:bg-gray-200"
                        }
                    >

                        <span
                            onClick={() => onConversationSelect(conversation)}
                            className="flex-1"
                        >
                            {conversation.title}
                        </span>

                        <button onClick={(event) => {
                            event.stopPropagation();
                            onConversationDelete(conversation);
                        }}
                            disabled={deletingConversationId === conversation.id}
                            className="ml-2 rounded px-2 py-1 text-sm text-red-500 hover:bg-red-100"
                        >
                            {deletingConversationId === conversation.id
                                ? "Deleting..."
                                : "Delete"
                            }

                        </button>
                    </div>
                ))}
            </div>
        </aside>
    );
}

export default Sidebar;