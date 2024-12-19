document.addEventListener("DOMContentLoaded", () => {
    console.log("Page loaded!");

    // Get references to key elements
    const formatSelect = document.querySelector("select[name='format']");
    const resolutionSelect = document.getElementById("resolution");
    const message = document.getElementById("resolution-message");
    const form = document.getElementById('download-form');
    const spinner = document.getElementById('loading-spinner');
    const loadingText = document.getElementById('loading-text');

    // Handle format selection changes
    formatSelect.addEventListener("change", function () {
        if (this.value === "audio") {
            // Disable resolution dropdown for audio
            resolutionSelect.disabled = true;
            resolutionSelect.style.opacity = "0.5"; // Visual cue
            message.textContent = "Resolution is not applicable for audio.";
        } else {
            // Enable resolution dropdown for video
            resolutionSelect.disabled = false;
            resolutionSelect.style.opacity = "1"; // Reset visual cue
            message.textContent = ""; // Clear message
        }
    });

    // Handle form submission
    form.addEventListener('submit', () => {
        // Show spinner and loading text
        spinner.style.display = 'block';
        loadingText.style.display = 'block';
    });
});
