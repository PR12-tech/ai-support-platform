import type { UserResponse } from "../types/api";

type HeaderProps = {
    currentUser: UserResponse | null;
    onLogout: () => void;
    onToggleSidebar?: () => void;
};

function Header({ currentUser, onLogout, onToggleSidebar }: HeaderProps) {
    return (
        <header className="flex h-16 items-center justify-between border-b border-slate-200 bg-white px-6 shadow-sm">
            <div className="flex items-center gap-3">
                {/* Burger menu for smaller screens */}
                <button
                    onClick={onToggleSidebar}
                    className="rounded-lg p-2 text-slate-500 hover:bg-slate-100 focus:outline-none lg:hidden"
                    aria-label="Toggle Sidebar"
                >
                    <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                </button>

                <div className="flex items-center gap-2">
                    <span className="text-2xl">🛒</span>
                    <span className="text-lg font-bold text-slate-900 tracking-tight">NovaCart Support</span>
                </div>
            </div>

            <div className="flex items-center gap-4">
                {currentUser && (
                    <div className="flex items-center gap-3 border-r border-slate-200 pr-4">
                        {/* Initials avatar */}
                        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-indigo-100 font-semibold text-indigo-700 uppercase">
                            {currentUser.username.slice(0, 2)}
                        </div>
                        <div className="hidden flex-col text-left sm:flex">
                            <span className="text-xs font-semibold text-slate-800 leading-none">{currentUser.username}</span>
                            <span className="mt-0.5 text-[10px] text-slate-400 leading-none">{currentUser.email}</span>
                        </div>
                    </div>
                )}

                <button
                    onClick={onLogout}
                    className="flex items-center gap-1.5 rounded-lg border border-slate-300 px-3.5 py-1.5 text-xs font-semibold text-slate-700 shadow-sm transition hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-indigo-100"
                >
                    <span>Logout</span>
                    <svg className="h-3.5 w-3.5 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                </button>
            </div>
        </header>
    );
}

export default Header;