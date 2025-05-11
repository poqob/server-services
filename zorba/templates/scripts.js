const funnyEmojis = [
    '😜', '🤪', '🥳', '😂', '🤣', '😎', '😏', '😱', '🥴', '😭', '💀', '🤓', '😌', '💅', '😃', '🤩', '🤯', '🤗', '🤭', '🥰',
    '🍕', '🚀', '🚗', '🍆', '🍑', '🍌', '💩', '🔥', '💥', '🚨', '🎉', '🎊', '🎈', '🌈', '☀️', '🌙', '⭐', '✨', '💫', '💦'
];

function generateEmojiCombo() {
    const combo = [];
    for (let i = 0; i < 3; i++) {
        const randomIndex = Math.floor(Math.random() * funnyEmojis.length);
        combo.push(funnyEmojis[randomIndex]);
    }
    return combo.join('');
}

function getKufur() {
    fetch('https://poqob.site/zorba-api')
        .then(response => response.json())
        .then(data => {
            const emojiCombo = generateEmojiCombo();
            document.getElementById('kufur-display').textContent = `${data.kufur} ${emojiCombo}`;
        })
        .catch(error => {
            console.error('Hata:', error);
            document.getElementById('kufur-display').textContent = 'Bir hata oluştu. 😵';
        });
}