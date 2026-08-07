document.addEventListener("DOMContentLoaded", () => {

    const progressBars = document.querySelectorAll(".progress-fill");

    progressBars.forEach(bar => {

        const value = parseFloat(bar.dataset.progress) || 0;

        bar.style.width = `${value}%`;

    });

});