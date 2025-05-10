// Kalp animasyonu fonksiyonlarını koruyorum
function createHearts() {
    const body = document.querySelector('body');
    const maxHearts = 20;
    
    for (let i = 0; i < maxHearts; i++) {
        setTimeout(() => {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            
            const size = Math.random() * 20 + 10;
            heart.style.width = size + 'px';
            heart.style.height = size + 'px';
            
            const x = Math.random() * window.innerWidth;
            const y = Math.random() * window.innerHeight;
            heart.style.left = x + 'px';
            heart.style.top = y + 'px';
            
            body.appendChild(heart);
            
            setTimeout(() => {
                heart.remove();
            }, 1500);
        }, i * 300);
    }
}

// Sayaç fonksiyonları
function updateCountdown() {
    // 16 Şubat 2025 tarihinden başlama
    const startDate = new Date(2025, 1, 16); // Ay indeksi 0'dan başlar, bu nedenle 1 = Şubat
    const currentDate = new Date();
    
    // İki tarih arasındaki farkı milisaniye cinsinden hesapla
    const diff = currentDate - startDate;
    
    // Eğer tarih henüz gelmemiş ise tüm değerleri 0 olarak göster
    if (diff < 0) {
        document.getElementById("months").textContent = "0";
        document.getElementById("days").textContent = "0";
        document.getElementById("hours").textContent = "0";
        document.getElementById("minutes").textContent = "0";
        return;
    }
    
    // Millisaniyeyi dakika, saat, gün ve aya dönüştür
    const minutes = Math.floor(diff / (1000 * 60)) % 60;
    const hours = Math.floor(diff / (1000 * 60 * 60)) % 24;
    const days = Math.floor(diff / (1000 * 60 * 60 * 24)) % 30; // Ortalama bir ay için
    
    // Ay hesaplaması
    let monthsDiff = (currentDate.getFullYear() - startDate.getFullYear()) * 12;
    monthsDiff += currentDate.getMonth() - startDate.getMonth();
    
    // Eğer günler, ayın gününden küçükse 1 ay azalt
    if (currentDate.getDate() < startDate.getDate()) {
        monthsDiff--;
    }
    
    // Değerleri HTML elementlerine yaz
    document.getElementById("months").textContent = monthsDiff;
    document.getElementById("days").textContent = days;
    document.getElementById("hours").textContent = hours;
    document.getElementById("minutes").textContent = minutes;
}

// Sayfa yüklendiğinde ve her dakika sayacı güncelle
document.addEventListener("DOMContentLoaded", function() {
    updateCountdown();
    setInterval(updateCountdown, 60000); // Her dakika güncelle
});

// Kalp animasyonu zamanlayıcıları
setInterval(createHearts, 6000);
setTimeout(createHearts, 1000);