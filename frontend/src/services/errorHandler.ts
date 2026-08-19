import axios from "axios";

export function getErrorMessage(error: unknown): string {

    if (axios.isAxiosError(error)) {

        if (error.code === "ECONNABORTED") {
            return "The request took too long. Please try again.";
        }

        if (!error.response) {
            return "Unable to connect to the backend.";
        }

        if (error.response.status >= 500) {
            return "Something went wrong on the server. Please try again.";
        }

        if (error.response.status === 404) {
            return "The requested resource was not found.";
        }

        if (error.response.status === 401) {
            if (error.config?.url?.endsWith("/login")) {
                return "Invalid username or password.";
            }
            return "You are not authorized to perform this action.";
        }

        if (error.response.status >= 400) {
            return "The request could not be completed.";
        }
    }

    return "Something went wrong. Please try again.";
}