document.addEventListener('DOMContentLoaded', function() {
    const aiForm = document.getElementById('ai-form');
    const loadingScreen = document.getElementById('loading-screen');
    const resultTitle = document.querySelector('.result-title');

    // Tampilkan loading saat submit
    if (aiForm) {
        aiForm.addEventListener('submit', function() {
            loadingScreen.style.display = 'flex';
            const btn = this.querySelector('button[type="submit"]');
            
            // animasi tombol menjadi disabled
            btn.innerHTML = '<span style="transform: translateZ(15px)"><i class="fas fa-cube fa-spin me-2"></i>Mencari di Dimensi...</span>';
            btn.classList.add('disabled');
            btn.style.pointerEvents = 'none';
        });
    }

    // Auto-scroll jika ada hasil
    if (resultTitle) {
        // Beri sedikit delay untuk membiarkan animasi 3D render pertama
        setTimeout(() => {
            resultTitle.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }, 300);
    }
});