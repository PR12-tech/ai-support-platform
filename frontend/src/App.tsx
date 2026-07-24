import { useState } from "react";
import Header from "./components/Header";
import MainLayout from "./components/MainLayout";

function App() {
  const [conversations, setConversations] = useState([
    "Order Refund",
    "Shipping Delay",
    "Payment Failed",
    "SQL Analytics",
]);

const [selectedConversation, setSelectedConversation] = 
  useState("Order Refund")


function handleNewChat() {
  setConversations([
    ...conversations,
    "New Conversation",
  ]);
}

function handleConversationSelect(conversation: string) {
  setSelectedConversation(conversation)
}

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="flex min-h-screen flex-col">
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