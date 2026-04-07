function getStatusAndColor(percent) {
    if (percent < 20) {
        return { status: "Excellent", color: "bg-emerald-500", text: "text-emerald-500" };
    } else if (percent < 50) {
        return { status: "Good", color: "bg-emerald-500", text: "text-emerald-500" };
    } else if (percent < 80) {
        return { status: "Moderate", color: "bg-yellow-500", text: "text-yellow-500" };
    } else if (percent < 100) {
        return { status: "Warning", color: "bg-yellow-500", text: "text-yellow-500" };
    } else {
        return { status: "Over Budget", color: "bg-red-500", text: "text-red-500" };
    }
}


function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const main = document.querySelector("main");
    const btn = document.getElementById("toggle-btn");

    const isHidden = sidebar.classList.contains("hidden");

    if (isHidden) {
        sidebar.classList.remove("hidden");
        main.classList.add("ml-56");
        btn.classList.add("bg-emerald-100");
    } else {
        sidebar.classList.add("hidden");
        main.classList.remove("ml-56");
        btn.classList.remove("bg-emerald-100");
    }
}

function updateGreeting() {
    const now = new Date();
    const hour = now.getHours();

    let greeting;

    if (hour >= 5 && hour < 12) {
        greeting = "Good Morning ☀️";
    } else if (hour >= 12 && hour < 17) {
        greeting = "Good Afternoon 🌤️";
    } else if (hour >= 17 && hour < 21) {
        greeting = "Good Evening 🌇";
    } else {
        greeting = "Good Night 🌙";
    }

    const dateOptions = { weekday: "long", year: "numeric", month: "long", day: "numeric" };
    const dateString = now.toLocaleDateString("en-IN", dateOptions);

    document.getElementById("greeting-text").textContent = greeting;
    document.getElementById("date-text").textContent = dateString;
}
