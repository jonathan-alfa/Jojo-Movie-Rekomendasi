document.addEventListener('DOMContentLoaded', function() {
    const aiForm = document.getElementById('ai-form');
    const loadingScreen = document.getElementById('loading-screen');
    const resultTitle = document.querySelector('.result-title');

    // Tampilkan loading saat submit
    if (aiForm) {
        aiForm.addEventListener('submit', function() {
            loadingScreen.style.display = 'flex';
            const btn = this.querySelector('button[type="submit"]');
            btn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Memproses...';
            btn.classList.add('disabled');
        });
    }

    // Auto-scroll jika ada hasil
    if (resultTitle) {
        resultTitle.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
});