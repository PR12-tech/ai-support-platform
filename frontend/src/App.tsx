import { useEffect, useState } from "react";
import Header from "./components/Header";
import MainLayout from "./components/MainLayout";
import type { Conversation } from "./types/conversation";
import { getConversations, createConversation, deleteHistory } from "./services/ChatService";
import { getErrorMessage } from "./services/errorHandler";


function App() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isLoadingConversations, setIsLoadingConversations] = useState(true);
  const [isCreatingConversation, setIsCreatingConversation] = useState(false);
  const [deletingConversationId, setDeletingConversationId] = useState<string | null>(null);

  async function loadConversations() {

    try {

      const response = await getConversations();

      const loadedConversations = response.conversations.map(
        (conversation) => ({
          id: conversation.session_id,
          title: conversation.title,
        })
      );

      setConversations(loadedConversations);

      if (loadedConversations.length > 0) {

        setSelectedConversation(
          loadedConversations[0]
        );

      }

    } catch (error) {

      console.error(error);

      setErrorMessage(
        getErrorMessage(error)
      );

    } finally {

      setIsLoadingConversations(false);

    }

  }

  useEffect(() => {

    loadConversations();

  }, []);

  const [selectedConversation, setSelectedConversation] =
    useState<Conversation | null>(null);


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

      setConversations((previous) => [
        ...previous,
        newConversation,
      ]);

      setSelectedConversation(newConversation);

    } catch (error) {

      console.error(error);

      setErrorMessage(
        getErrorMessage(error)
      );
    } finally {

      setIsCreatingConversation(false);

    }
  }


  function handleConversationSelect(conversation: Conversation) {
    setSelectedConversation(conversation)
  }

  async function handleConversationDelete(
    conversation: Conversation
  ) {

    if (deletingConversationId) {
      return;
    }

    const confirmed = window.confirm(
      `Delete "${conversation.title}"?`
    );

    if (!confirmed) {
      return;
    }

    try {

      setDeletingConversationId(conversation.id);

      await deleteHistory(conversation.id);

      const remainingConversations =
        conversations.filter(
          (item) => item.id !== conversation.id
        );

      setConversations(remainingConversations);

      if (
        selectedConversation?.id === conversation.id
      ) {

        if (remainingConversations.length > 0) {

          setSelectedConversation(
            remainingConversations[0]
          );

        } else {

          setSelectedConversation(null);

        }

      }

    } catch (error) {

      console.error(error);

      setErrorMessage(
        getErrorMessage(error)
      );

    } finally {

      setDeletingConversationId(null);

    }

  }

  return (
    <div className="h-screen bg-gray-100">
      <div className="flex h-full flex-col">

        <Header />

        {errorMessage && (
          <div className="mx-4 mt-4 rounded-md border border-red-200 bg-red-50 p-3 text-sm text-red-700">
            {errorMessage}
          </div>
        )}

        {isLoadingConversations ? (
          <div className="flex flex-1 items-center justify-center">
            <p className="text-gray-500">
              Loading conversations...
            </p>
          </div>
        ) : (

          selectedConversation && (
            <MainLayout
              conversations={conversations}
              selectedConversation={selectedConversation}
              onNewChat={handleNewChat}
              onConversationSelect={handleConversationSelect}
              onConversationDelete={handleConversationDelete}
              isCreatingConversation={isCreatingConversation}
              deletingConversationId={deletingConversationId}
            />
          )
        )}
      </div>
    </div>
  );
}

export default App