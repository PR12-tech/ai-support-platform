export type HistoryMessage = {
    role: "user" | "assistant";
    content: string;
    created_at: string;
};

export type HistoryResponse = {
    session_id: string;
    history: HistoryMessage[];
};

export type ConversationResponse = {
    session_id: string;
    title: string;
    created_at: string;
};

export type ConversationListResponse = {
    conversations: ConversationResponse[];
};

export type UserResponse = {
    id: number;
    username: string;
    email: string;
};