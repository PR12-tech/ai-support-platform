import api from "./api";

export type LoginRequest = {
    username: string;
    password: string;
};

export type LoginResponse = {
    access_token: string;
    token_type: string;
};

export async function login(
    request: LoginRequest
) : Promise<LoginResponse> {

    const formData = new URLSearchParams();

    formData.append(
        "username",
        request.username
    );

    formData.append(
        "password",
        request.password
    );

    const response = await api.post<LoginResponse>(
        "/login",
        formData,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );

    localStorage.setItem(
        "access_token",
        response.data.access_token
    );

    return response.data;

}