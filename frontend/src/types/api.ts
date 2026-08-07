export type HistoryMessage = {
    role: "user" | "assistant";
    content: string;
    created_at: string;
};

export type HistoryResponse = {
    session_id: string;
    history: HistoryMessage[];
};