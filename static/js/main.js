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

    // Modal functionality
    const modal = document.getElementById('infoModal');
    const span = document.getElementsByClassName('close')[0];

    // When user clicks the info button, open modal
    window.showInfo = function() {
        const modal = document.getElementById('infoModal');
        modal.style.display = 'flex';
    }

    // When user clicks on (x), close modal
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // When user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
}); 