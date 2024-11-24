// Add any necessary JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    // Fade out alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        });
    }, 5000);
}); 