const API_URL = "http://127.0.0.1:5000/api/expenses/";
const INSIGHTS_URL = "http://127.0.0.1:5000/api/expenses/ai-insights";

async function loadDashboard() {
    const response = await fetch(API_URL);
    const expenses = await response.json();

    updateTotalSpending(expenses);
    updateMonthSpending(expenses);
    showRecentExpenses(expenses);
    drawPieChart(expenses);
}

function updateTotalSpending(expenses) {
    let total = 0;

    expenses.forEach((expense) => {
        total += expense.amount;
    });

    document.getElementById("total-spending").textContent = "₹" + total;
}

function updateMonthSpending(expenses) {
    const now = new Date();
    const currentMonth = now.getMonth();
    const currentYear = now.getFullYear();

    let total = 0;

    expenses.forEach((expense) => {
        const expenseDate = new Date(expense.created_at);
        if (expenseDate.getMonth() === currentMonth && 
            expenseDate.getFullYear() === currentYear) {
            total += expense.amount;
        }
    });

    document.getElementById("month-spending").textContent = "₹" + total;
}

function showRecentExpenses(expenses) {
    const tbody = document.getElementById("recent-expenses");
    tbody.innerHTML = "";

    const recent = expenses.slice(-5).reverse();

    recent.forEach((expense) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td class="px-4 py-3">${expense.category}</td>
            <td class="px-4 py-3">${expense.description || "-"}</td>
            <td class="px-4 py-3">₹${expense.amount}</td>
            <td class="px-4 py-3">${new Date(expense.created_at).toLocaleDateString("en-IN")}</td>
        `;
        tbody.appendChild(row);
    });
}

function drawPieChart(expenses) {
    // step 1 - calculate total per category
    const categoryTotals = {};

    expenses.forEach((expense) => {
        if (categoryTotals[expense.category]) {
            categoryTotals[expense.category] += expense.amount;
        } else {
            categoryTotals[expense.category] = expense.amount;
        }
    });

    // step 2 - separate labels and values
    const labels = Object.keys(categoryTotals);
    const values = Object.values(categoryTotals);

    // step 3 - draw the chart
    const ctx = document.getElementById("pie-chart").getContext("2d");
    new Chart(ctx, {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: [
                    "#3B82F6",
                    "#8B5CF6",
                    "#10B981",
                    "#F59E0B",
                    "#EF4444",
                    "#EC4899"
                ]
            }]
        }
    });
}

async function fetchInsights() {
    const box = document.getElementById("insights-box");
    box.textContent = "Loading insights...";

    try {
        const response = await fetch(INSIGHTS_URL);
        const data = await response.json();
        box.textContent = data.insights;
    } catch (error) {
        box.textContent = "Failed to load insights. Try again!";
    }
}
// run on page load
loadDashboard();
fetchInsights();