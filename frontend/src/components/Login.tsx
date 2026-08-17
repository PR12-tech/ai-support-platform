import { useState } from "react";
import { getErrorMessage } from "../services/errorHandler";
import { login } from "../services/AuthService";

type LoginProps = {
    onLoginSuccess: () => void;
};

function Login({ onLoginSuccess }: LoginProps) {

    const [username, setUsername] = useState("");
const [password, setPassword] = useState("");
const [errorMessage, setErrorMessage] = useState<string | null>(null);
const [isLoading, setIsLoading] = useState(false);

async function handleSubmit(
    event: React.SubmitEvent<HTMLFormElement>
) {

    event.preventDefault();

    setErrorMessage(null);

    try {

        setIsLoading(true);

        await login({
            username,
            password,
        });

        onLoginSuccess();

    } catch (error) {

        console.error(error);

        setErrorMessage(
            getErrorMessage(error)
        );

    } finally {

        setIsLoading(false);

    }
    
}

return (
        <div className="flex min-h-screen items-center justify-center bg-gray-100">

            <div className="w-full max-w-md rounded-lg bg-white p-8 shadow-md">

                <h1 className="mb-2 text-2xl font-bold">
                    AI Customer Support Platform
                </h1>

                <p className="mb-6 text-sm text-gray-500">
                    Login to continue
                </p>

                {errorMessage && (
                    <div className="mb-4 rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-700">
                        {errorMessage}
                    </div>
                )}

                <form
                    onSubmit={handleSubmit}
                    className="space-y-4"
                >

                    <div>
                        <label
                            htmlFor="username"
                            className="mb-1 block text-sm font-medium text-gray-700"
                        >
                            Username or Email
                        </label>

                        <input
                            id="username"
                            type="text"
                            value={username}
                            onChange={(event) =>
                                setUsername(event.target.value)
                            }
                            required
                            className="w-full rounded-md border border-gray-300 px-3 py-2 outline-none focus:border-blue-500"
                            placeholder="Enter username or email"
                        />
                    </div>

                    <div>
                        <label
                            htmlFor="password"
                            className="mb-1 block text-sm font-medium text-gray-700"
                        >
                            Password
                        </label>

                        <input
                            id="password"
                            type="password"
                            value={password}
                            onChange={(event) =>
                                setPassword(event.target.value)
                            }
                            required
                            className="w-full rounded-md border border-gray-300 px-3 py-2 outline-none focus:border-blue-500"
                            placeholder="Enter password"
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={isLoading}
                        className="w-full rounded-md bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
                    >
                        {isLoading ? "Logging in..." : "Login"}
                    </button>

                </form>

            </div>

        </div>
    );
}

export default Login;