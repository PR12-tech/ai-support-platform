import { useEffect, useState, useCallback } from "react";
import Header from "./components/Header";
import MainLayout from "./components/MainLayout";
import type { Conversation } from "./types/conversation";
import type { UserResponse } from "./types/api";
import { getConversations, createConversation, deleteHistory } from "./services/ChatService";
import { getCurrentUser } from "./services/AuthService";
import { getErrorMessage } from "./services/errorHandler";
import Login from "./components/Login";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    Boolean(localStorage.getItem("access_token"))
  );
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isLoadingConversations, setIsLoadingConversations] = useState(true);
  const [isCreatingConversation, setIsCreatingConversation] = useState(false);
  const [deletingConversationId, setDeletingConversationId] = useState<string | null>(null);
  
  const [currentUser, setCurrentUser] = useState<UserResponse | null>(null);
  const [isMobileSidebarOpen, setIsMobileSidebarOpen] = useState(false);
  const [selectedConversation, setSelectedConversation] = useState<Conversation | null>(null);

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const handleApiError = useCallback((error: any) => {
    console.error(error);
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token");
      setIsAuthenticated(false);
      setErrorMessage("Session expired. Please log in again.");
    } else {
      setErrorMessage(getErrorMessage(error));
    }
  }, []);

  const loadCurrentUser = useCallback(async () => {
    try {
      const profile = await getCurrentUser();
      setCurrentUser(profile);
      return true;
    } catch (error) {
      handleApiError(error);
      return false;
    }
  }, [handleApiError]);

  const loadConversations = useCallback(async () => {
    try {
      setIsLoadingConversations(true);
      const response = await getConversations();

      const loadedConversations = response.conversations.map(
        (conversation) => ({
          id: conversation.session_id,
          title: conversation.title,
        })
      );

      setConversations(loadedConversations);

      if (loadedConversations.length > 0) {
        setSelectedConversation(loadedConversations[0]);
      }
    } catch (error) {
      handleApiError(error);
    } finally {
      setIsLoadingConversations(false);
    }
  }, [handleApiError]);

  useEffect(() => {
    if (isAuthenticated) {
      Promise.resolve().then(async () => {
        const ok = await loadCurrentUser();
        if (ok) {
          loadConversations();
        }
      });
    } else {
      Promise.resolve().then(() => {
        setCurrentUser(null);
      });
    }
  }, [isAuthenticated, loadCurrentUser, loadConversations]);

  function handleLoginSuccess() {
    setIsAuthenticated(true);
  }

  function handleLogout() {
    localStorage.removeItem("access_token");
    setIsAuthenticated(false);
    setSelectedConversation(null);
    setConversations([]);
    setCurrentUser(null);
    setErrorMessage(null);
  }

  if (!isAuthenticated) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  async function handleNewChat() {
    if (isCreatingConversation) {
      return;
    }

    try {
      setIsCreatingConversation(true);
      const response = await createConversation();

      const newConversation: Conversation = {
        id: response.session_id,
        title: response.title,
      };

      setConversations((previous) => [...previous, newConversation]);
      setSelectedConversation(newConversation);
    } catch (error) {
      handleApiError(error);
    } finally {
      setIsCreatingConversation(false);
    }
  }

  function handleConversationSelect(conversation: Conversation) {
    setSelectedConversation(conversation);
  }

  async function handleConversationDelete(conversation: Conversation) {
    if (deletingConversationId) {
      return;
    }

    const confirmed = window.confirm(`Delete "${conversation.title}"?`);
    if (!confirmed) {
      return;
    }

    try {
      setDeletingConversationId(conversation.id);
      await deleteHistory(conversation.id);

      const remainingConversations = conversations.filter(
        (item) => item.id !== conversation.id
      );

      setConversations(remainingConversations);

      if (selectedConversation?.id === conversation.id) {
        if (remainingConversations.length > 0) {
          setSelectedConversation(remainingConversations[0]);
        } else {
          setSelectedConversation(null);
        }
      }
    } catch (error) {
      handleApiError(error);
    } finally {
      setDeletingConversationId(null);
    }
  }

  return (
    <div className="h-screen bg-slate-50">
      <div className="flex h-full flex-col">
        <Header
          currentUser={currentUser}
          onLogout={handleLogout}
          onToggleSidebar={() => setIsMobileSidebarOpen(!isMobileSidebarOpen)}
        />

        {errorMessage && (
          <div className="mx-6 mt-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800">
            <div className="flex justify-between items-center">
              <div className="flex gap-2">
                <span>⚠️</span>
                <span>{errorMessage}</span>
              </div>
              <button 
                onClick={() => setErrorMessage(null)}
                className="text-red-500 hover:text-red-700 font-bold"
              >
                ✕
              </button>
            </div>
          </div>
        )}

        {isLoadingConversations ? (
          <div className="flex flex-1 items-center justify-center">
            <div className="flex flex-col items-center gap-3">
              <svg className="h-8 w-8 animate-spin text-indigo-600" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              <p className="text-sm font-medium text-slate-500">Loading support history...</p>
            </div>
          </div>
        ) : (
          <MainLayout
            conversations={conversations}
            selectedConversation={selectedConversation}
            onNewChat={handleNewChat}
            onConversationSelect={handleConversationSelect}
            onConversationDelete={handleConversationDelete}
            isCreatingConversation={isCreatingConversation}
            deletingConversationId={deletingConversationId}
            isMobileSidebarOpen={isMobileSidebarOpen}
            onCloseMobileSidebar={() => setIsMobileSidebarOpen(false)}
          />
        )}
      </div>
    </div>
  );
}

export default App;