import api from "./api";
import type { HistoryResponse } from "../types/api";
import type { ConversationListResponse, ConversationResponse } from "../types/api";

export type ChatRequest = {
    question: string;
    session_id: string;
};

export async function askQuestion(request: ChatRequest) {

    const response = await api.post("/ask", request);

    return response.data;
}

export async function getHistory(
    sessionId: string
): Promise<HistoryResponse> {

    const response = await api.get<HistoryResponse>(
        `/history/${sessionId}`
    );

    return response.data;
}

export async function deleteHistory(sessionId: string) {

    const response = await api.delete(`/history/${sessionId}`);

    return response.data;
}

export async function getConversations(): Promise<ConversationListResponse> {

    const response = await api.get<ConversationListResponse>(
        "/conversations"
    );

    return response.data;
    
}

export async function createConversation(): Promise<ConversationResponse> {
    
    const response = await api.post<ConversationResponse>(
        "/conversations"
    );

    return response.data;
}