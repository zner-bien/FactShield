document.addEventListener("DOMContentLoaded", () => {

    /* ==========================================
       TAB SWITCHING
    ========================================== */

    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach(button => {

        button.addEventListener("click", () => {

            const target = button.dataset.tab;

            tabButtons.forEach(btn => btn.classList.remove("active"));
            tabContents.forEach(content => content.classList.remove("active"));

            button.classList.add("active");

            document
                .getElementById(target)
                .classList.add("active");

        });

    });

    /* ==========================================
       FILE UPLOAD
    ========================================== */

    const uploadBox = document.querySelector(".upload-box");
    const fileInput = uploadBox.querySelector("input[type='file']");
    const uploadTitle = uploadBox.querySelector("h3");
    const uploadText = uploadBox.querySelector("p");

    uploadBox.addEventListener("click", (e) => {

        if (e.target !== fileInput) {
            fileInput.click();
        }

    });

    fileInput.addEventListener("change", () => {

        if (fileInput.files.length > 0) {

            const file = fileInput.files[0];

            uploadTitle.textContent = file.name;
            uploadText.textContent = `${(file.size / 1024).toFixed(1)} KB`;

        }

    });

    uploadBox.addEventListener("dragover", (e) => {

        e.preventDefault();
        uploadBox.classList.add("dragover");

    });

    uploadBox.addEventListener("dragleave", () => {

        uploadBox.classList.remove("dragover");

    });

    uploadBox.addEventListener("drop", (e) => {

        e.preventDefault();
        uploadBox.classList.remove("dragover");

        if (e.dataTransfer.files.length > 0) {

            fileInput.files = e.dataTransfer.files;

            const file = e.dataTransfer.files[0];

            uploadTitle.textContent = file.name;
            uploadText.textContent = `${(file.size / 1024).toFixed(1)} KB`;

        }

    });

    /* ==========================================
       FORM VALIDATION
    ========================================== */

    const form = document.querySelector("form");
    const analyzeButton = document.querySelector(".analyze-btn");

    form.addEventListener("submit", (e) => {

        const activeTab =
            document.querySelector(".tab-btn.active").dataset.tab;

        if (activeTab === "text") {

            const text =
                document.querySelector("#text textarea").value.trim();

            if (!text) {

                e.preventDefault();

                alert("Please paste a news article.");

                return;

            }

        }

        if (activeTab === "url") {

            const url =
                document.querySelector("#url input").value.trim();

            if (!url) {

                e.preventDefault();

                alert("Please enter a news article URL.");

                return;

            }

        }

        if (activeTab === "upload") {

            if (fileInput.files.length === 0) {

                e.preventDefault();

                alert("Please upload a file.");

                return;

            }

        }

        /* Loading State */

        analyzeButton.disabled = true;

        analyzeButton.innerHTML = `
            <i data-lucide="loader-circle"></i>
            Analyzing...
        `;

        lucide.createIcons();

        // Allow the form to submit normally to Flask
    });

});