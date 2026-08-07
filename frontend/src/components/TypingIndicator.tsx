function TypingIndicator() {
    return (
        <div className="mb-4 flex justify-start">
            <div className="rounded-lg bg-gray-200 px-4 py-3">
                <div className="flex gap-1">
                    <span className="h-2 w-2 animate-bounce rounded-full bg-gray-500"></span>
                    <span className="h-2 w-2 animate-bounce rounded-full bg-gray-500 [animation-delay:150ms]"></span>
                    <span className="h-2 w-2 animate-bounce rounded-full bg-gray-500 [animation-delay:300ms]"></span>
                </div>
            </div>
        </div>
    );
}
   
export default TypingIndicator;