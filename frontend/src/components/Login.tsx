import { useState } from "react";
import { getErrorMessage } from "../services/errorHandler";
import { login, register } from "../services/AuthService";

type LoginProps = {
    onLoginSuccess: () => void;
};

function Login({ onLoginSuccess }: LoginProps) {
    const [isRegistering, setIsRegistering] = useState(false);
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);

    async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setErrorMessage(null);

        try {
            setIsLoading(true);

            if (isRegistering) {
                await register({
                    username,
                    email,
                    password,
                });
                setIsRegistering(false);
                setPassword("");
                setErrorMessage(null);
            } else {
                await login({
                    username,
                    password,
                });
                onLoginSuccess();
            }
        } catch (error) {
            console.error(error);
            setErrorMessage(getErrorMessage(error));
        } finally {
            setIsLoading(false);
        }
    }

    return (
        <div className="flex min-h-screen items-center justify-center bg-slate-50 px-4 py-12 sm:px-6 lg:px-8">
            <div className="flex w-full max-w-4xl overflow-hidden rounded-2xl bg-white shadow-xl">
                
                {/* Left Side: Marketing/Value Prop Banner */}
                <div className="hidden w-1/2 bg-indigo-600 p-12 text-white md:flex md:flex-col md:justify-between">
                    <div>
                        <div className="flex items-center gap-2 text-2xl font-bold tracking-tight">
                            <span className="text-3xl">🛒</span>
                            <span>NovaCart Support</span>
                        </div>
                        <p className="mt-2 text-indigo-100">Intelligent enterprise support center</p>
                    </div>

                    <div className="space-y-6">
                        <div className="flex gap-4">
                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/50 text-xl">
                                📦
                            </div>
                            <div>
                                <h3 className="font-semibold">Instant Order Tracking</h3>
                                <p className="text-sm text-indigo-100">Check shipment statuses, estimated delivery windows, and details in seconds.</p>
                            </div>
                        </div>

                        <div className="flex gap-4">
                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/50 text-xl">
                                🎫
                            </div>
                            <div>
                                <h3 className="font-semibold">Ticket & Issue Management</h3>
                                <p className="text-sm text-indigo-100">Create, monitor, and query customer support tickets directly through chat.</p>
                            </div>
                        </div>

                        <div className="flex gap-4">
                            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/50 text-xl">
                                📘
                            </div>
                            <div>
                                <h3 className="font-semibold">Knowledge Grounded</h3>
                                <p className="text-sm text-indigo-100">Our assistant is backed by up-to-date company policies and knowledge documents.</p>
                            </div>
                        </div>
                    </div>

                    <div className="text-xs text-indigo-200">
                        &copy; 2026 NovaCart Technologies Pvt. Ltd. All rights reserved.
                    </div>
                </div>

                {/* Right Side: Login/Register Form */}
                <div className="w-full p-8 md:w-1/2 lg:p-12">
                    <div className="flex items-center justify-between">
                        <h2 className="text-2xl font-bold text-slate-900">
                            {isRegistering ? "Get Started" : "Welcome Back"}
                        </h2>
                        <button
                            onClick={() => {
                                setIsRegistering(!isRegistering);
                                setPassword("");
                                setEmail("");
                                setUsername("");
                                setErrorMessage(null);
                            }}
                            className="text-sm font-semibold text-indigo-600 hover:text-indigo-500"
                        >
                            {isRegistering ? "Sign In" : "Register"}
                        </button>
                    </div>

                    <p className="mt-2 text-sm text-slate-500">
                        {isRegistering
                            ? "Create your support profile to proceed."
                            : "Access your customer support space."}
                    </p>

                    {errorMessage && (
                        <div className="mt-6 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800">
                            <div className="flex gap-2">
                                <span className="font-bold">⚠️</span>
                                <span>{errorMessage}</span>
                            </div>
                        </div>
                    )}

                    <form onSubmit={handleSubmit} className="mt-8 space-y-6">
                        <div className="space-y-4">
                            <div>
                                <label
                                    htmlFor="username"
                                    className="block text-xs font-semibold uppercase tracking-wider text-slate-600"
                                >
                                    {isRegistering ? "Username" : "Username or Email"}
                                </label>
                                <input
                                    id="username"
                                    type="text"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    required
                                    className="mt-1 w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-sm placeholder-slate-400 outline-none transition focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100"
                                    placeholder={
                                        isRegistering
                                            ? "e.g., demo_user1"
                                            : "Enter your username or email"
                                    }
                                />
                            </div>

                            {isRegistering && (
                                <div>
                                    <label
                                        htmlFor="email"
                                        className="block text-xs font-semibold uppercase tracking-wider text-slate-600"
                                    >
                                        Email Address
                                    </label>
                                    <input
                                        id="email"
                                        type="email"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        required
                                        className="mt-1 w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-sm placeholder-slate-400 outline-none transition focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100"
                                        placeholder="e.g., user@novacart.com"
                                    />
                                </div>
                            )}

                            <div>
                                <label
                                    htmlFor="password"
                                    className="block text-xs font-semibold uppercase tracking-wider text-slate-600"
                                >
                                    Password
                                </label>
                                <input
                                    id="password"
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    required
                                    className="mt-1 w-full rounded-lg border border-slate-300 px-3.5 py-2.5 text-sm placeholder-slate-400 outline-none transition focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100"
                                    placeholder="Enter your password"
                                />
                            </div>
                        </div>

                        <button
                            type="submit"
                            disabled={isLoading}
                            className="flex w-full items-center justify-center rounded-lg bg-indigo-600 px-4 py-3 text-sm font-semibold text-white shadow transition hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            {isLoading ? (
                                <div className="flex items-center gap-2">
                                    <svg className="h-4 w-4 animate-spin text-white" fill="none" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                                    </svg>
                                    <span>Processing...</span>
                                </div>
                            ) : (
                                <span>{isRegistering ? "Create Account" : "Sign In"}</span>
                            )}
                        </button>
                    </form>
                </div>

            </div>
        </div>
    );
}

export default Login;