const API_URL = "https://spendwise-ai-mn0e.onrender.com/api/expenses/";

document.addEventListener("DOMContentLoaded", () => {

    // 🔥 SIDEBAR SYNC FIX
    const sidebar = document.getElementById("sidebar");
    const main = document.querySelector("main");
    const btn = document.getElementById("toggle-btn");

    const isHidden = sidebar.classList.contains("hidden");

    if (!isHidden) {
        main.classList.add("ml-56");
        btn.classList.add("bg-emerald-100");
    } else {
        main.classList.remove("ml-56");
        btn.classList.remove("bg-emerald-100");
    }

    // ✅ CATEGORY CHANGE
    document.getElementById("category").addEventListener("change", function() {
        const customDiv = document.getElementById("custom-category-div");
        if (this.value === "Other") {
            customDiv.classList.remove("hidden");
        } else {
            customDiv.classList.add("hidden");
        }
    });

    // ✅ FORM SUBMIT
    document.getElementById("expense-form").addEventListener("submit", async (e) => {
        e.preventDefault();

        const amount = document.getElementById("amount").value;
        const category = document.getElementById("category").value;
        const customCategory = document.getElementById("custom-category").value;
        const description = document.getElementById("description").value;

        const finalCategory = category === "Other" ? customCategory : category;

        await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                amount: Number(amount),
                category: finalCategory,
                description: description
            })
        });

        window.location.href = "expenses.html";
    });

    // ✅ GREETING
    updateGreeting();

});