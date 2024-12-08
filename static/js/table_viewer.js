document.addEventListener('DOMContentLoaded', function() {
    const table = document.querySelector('.data-table');
    
    // Row selection
    table.querySelectorAll('tbody tr').forEach(row => {
        row.addEventListener('click', function(e) {
            if (!e.target.closest('a') && !e.target.closest('button')) {
                this.classList.toggle('selected');
            }
        });
    });

    // Copyable cells
    const copyableCells = table.querySelectorAll('td:nth-child(2), td:nth-child(3)');
    copyableCells.forEach(cell => {
        cell.classList.add('clickable');
        
        cell.addEventListener('click', async function(e) {
            e.stopPropagation(); // Prevent row selection
            const text = this.textContent.trim();
            
            try {
                await navigator.clipboard.writeText(text);
                
                // Show tooltip
                const tooltip = document.createElement('div');
                tooltip.className = 'copy-tooltip';
                tooltip.textContent = 'Copied!';
                this.appendChild(tooltip);
                
                // Remove tooltip
                setTimeout(() => tooltip.remove(), 2000);
            } catch (err) {
                console.error('Failed to copy:', err);
            }
        });
    });

    // Hover effects for proof links
    const proofLinks = table.querySelectorAll('.proof-link');
    proofLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.closest('tr').classList.add('highlight');
        });
        
        link.addEventListener('mouseleave', function() {
            this.closest('tr').classList.remove('highlight');
        });
    });
}); 