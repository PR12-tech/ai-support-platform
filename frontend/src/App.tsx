import { useState } from "react";
import Header from "./components/Header";
import MainLayout from "./components/MainLayout";
import type { Conversation } from "./types/conversation";


function App() {
  const [conversations, setConversations] = useState<Conversation[]>([

    {

      id: "session-1",
      title: "Order Refund"

    },
    {

      id: "session-2",
      title: "Shipping Delay"

    },
    {

      id: "session-3",
      title: "Payment Failed",

    },
    {

      id: "session-4",
      title: "SQL Analytics",
      
    },
]);

const [selectedConversation, setSelectedConversation] = 
  useState<Conversation>(conversations[0]);


function handleNewChat() {
  
  const newConversation: Conversation = {
    id: crypto.randomUUID(),
    title: "New Conversation",
  };

  setConversations((previous) => [
    ...previous,
    newConversation,
  ]);

  setSelectedConversation(newConversation);

}


function handleConversationSelect(conversation: Conversation) {
  setSelectedConversation(conversation)
}

  return (
    <div className="h-screen bg-gray-100">
      <div className="flex h-full flex-col">
      <Header />
      <MainLayout 
      conversations={conversations}
      selectedConversation={selectedConversation}
      onNewChat={handleNewChat}
      onConversationSelect={handleConversationSelect}
      />
      </div>
    </div>
  )
}

export default App