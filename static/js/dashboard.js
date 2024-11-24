// Confirmation dialogs
function confirmAction(type) {
    const messages = {
        create: 'Are you sure you want to create a new table? This will drop any existing table.',
        truncate: 'Are you sure you want to remove all data? This cannot be undone.',
        delete: 'Are you sure you want to delete the table? A backup will be created first.'
    };

    return confirm(messages[type] || 'Are you sure?');
}

// Auto-dismiss alerts
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

// Add ripple effect to buttons
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('div');
        const rect = button.getBoundingClientRect();
        
        ripple.className = 'ripple';
        ripple.style.left = `${e.clientX - rect.left}px`;
        ripple.style.top = `${e.clientY - rect.top}px`;
        
        button.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
    });
}); 