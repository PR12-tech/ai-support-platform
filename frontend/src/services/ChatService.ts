import api from "./api";

type ChatRequest = {
    question: string;
    session_id: string;
};

export async function askQuestion(request: AskRequest) {

    const response = await api.post(
        "/ask",
        request
    );

    return response.data;
}