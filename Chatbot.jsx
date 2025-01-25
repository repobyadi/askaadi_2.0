import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
    const [query, setQuery] = useState("");
    const [responses, setResponses] = useState([]);

    const handleSend = async () => {
        if (!query) return;
        try {
            const response = await axios.post("http://localhost:8000/query", { query });
            setResponses([...responses, { user: query, bot: response.data }]);
            setQuery("");
        } catch (error) {
            console.error("Error fetching response:", error);
        }
    };

    return (
        <div style={{ margin: "20px" }}>
            <h1>Supplier & Product Chatbot</h1>
            <div>
                {responses.map((res, index) => (
                    <div key={index}>
                        <p><strong>User:</strong> {res.user}</p>
                        <p><strong>Bot:</strong> {JSON.stringify(res.bot)}</p>
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Ask me about products or suppliers..."
                style={{ marginRight: "10px" }}
            />
            <button onClick={handleSend}>Send</button>
        </div>
    );
};

export default Chatbot;
