document.addEventListener("DOMContentLoaded", () => {

    const button = document.getElementById("demoButton");

    if (!button) return;

    button.addEventListener("click", () => {

        const prediction = document.querySelector(".real");

        button.disabled = true;

        button.textContent = "Analyzing...";

        setTimeout(() => {

            const score = Math.floor(Math.random() * 10) + 90;

            document.querySelectorAll(".result-item span")[1].textContent =
                score + "%";

            prediction.textContent = "Likely Real";

            button.disabled = false;

            button.textContent = "Analyze Demo";

        }, 1800);

    });

});