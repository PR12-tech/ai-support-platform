import type { Conversation } from "../types/conversation";

type SidebarProps = {
    conversations: Conversation[];
    selectedConversation: Conversation | null;
    onNewChat: () => void;
    onConversationSelect: (conversation: Conversation) => void;
    onConversationDelete: (conversation: Conversation) => void;
    isCreatingConversation: boolean;
    deletingConversationId: string | null;
    isMobileOpen?: boolean;
    onCloseMobile?: () => void;
};

function Sidebar({
    conversations,
    selectedConversation,
    onNewChat,
    onConversationSelect,
    onConversationDelete,
    isCreatingConversation,
    deletingConversationId,
    isMobileOpen = false,
    onCloseMobile,
}: SidebarProps) {
    return (
        <>
            {/* Backdrop for Mobile Sidebar */}
            {isMobileOpen && (
                <div
                    onClick={onCloseMobile}
                    className="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-sm lg:hidden"
                />
            )}

            <aside
                className={`fixed inset-y-0 left-0 z-50 flex w-72 flex-col border-r border-slate-800 bg-slate-950 p-4 text-white transition-transform duration-300 lg:static lg:translate-x-0 ${
                    isMobileOpen ? "translate-x-0" : "-translate-x-full lg:translate-x-0"
                }`}
            >
                {/* Close button for Mobile */}
                <div className="flex justify-end lg:hidden">
                    <button
                        onClick={onCloseMobile}
                        className="rounded-lg p-2 text-slate-400 hover:bg-slate-850 hover:text-white"
                        aria-label="Close menu"
                    >
                        <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>

                <button
                    onClick={() => {
                        onNewChat();
                        if (onCloseMobile) onCloseMobile();
                    }}
                    disabled={isCreatingConversation}
                    className="flex w-full items-center justify-center gap-2 rounded-xl bg-indigo-600 px-4 py-3 font-semibold text-white shadow-md hover:bg-indigo-500 disabled:cursor-not-allowed disabled:opacity-50"
                >
                    {isCreatingConversation ? (
                        <>
                            <svg className="h-4 w-4 animate-spin text-white" fill="none" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                            </svg>
                            <span>Creating...</span>
                        </>
                    ) : (
                        <>
                            <span>💬</span>
                            <span>New Conversation</span>
                        </>
                    )}
                </button>

                <div className="mt-8 flex items-center justify-between px-2 text-xs font-semibold uppercase tracking-wider text-slate-500">
                    <span>Recent Chats</span>
                    <span className="rounded-full bg-slate-900 px-2 py-0.5 text-[10px]">
                        {conversations.length}
                    </span>
                </div>

                <div className="mt-4 flex-1 space-y-1 overflow-y-auto pr-1">
                    {conversations.length === 0 ? (
                        <div className="py-8 text-center text-sm text-slate-500">
                            No recent conversations.
                        </div>
                    ) : (
                        conversations.map((conversation) => {
                            const isSelected = conversation.id === selectedConversation?.id;
                            const isDeleting = deletingConversationId === conversation.id;
                            
                            return (
                                <div
                                    key={conversation.id}
                                    onClick={() => {
                                        onConversationSelect(conversation);
                                        if (onCloseMobile) onCloseMobile();
                                    }}
                                    className={`group flex items-center justify-between rounded-lg px-3 py-2.5 transition-all duration-200 cursor-pointer ${
                                        isSelected
                                            ? "bg-slate-900 text-white font-medium shadow-sm border-l-4 border-indigo-500"
                                            : "text-slate-400 hover:bg-slate-900 hover:text-slate-200"
                                    }`}
                                >
                                    <span className="flex-1 overflow-hidden text-ellipsis whitespace-nowrap text-sm">
                                        {conversation.title}
                                    </span>

                                    <button
                                        onClick={(event) => {
                                            event.stopPropagation();
                                            onConversationDelete(conversation);
                                        }}
                                        disabled={isDeleting}
                                        className="ml-2 hidden rounded p-1 text-slate-500 hover:bg-slate-800 hover:text-red-500 group-hover:block disabled:cursor-not-allowed"
                                        title="Delete Chat"
                                    >
                                        {isDeleting ? (
                                            <svg className="h-4 w-4 animate-spin text-slate-500" fill="none" viewBox="0 0 24 24">
                                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                                            </svg>
                                        ) : (
                                            <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                            </svg>
                                        )}
                                    </button>
                                </div>
                            );
                        })
                    )}
                </div>
            </aside>
        </>
    );
}

export default Sidebar;