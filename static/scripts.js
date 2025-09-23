// Tab switching logic
function switchTab(showCompare) {
    document.getElementById('tweetForm').classList.toggle('hidden', showCompare);
    document.getElementById('compareForm').classList.toggle('hidden', !showCompare);
    document.getElementById('tab-generate').classList.toggle('active', !showCompare);
    document.getElementById('tab-generate').setAttribute('aria-selected', !showCompare);
    document.getElementById('tab-compare').classList.toggle('active', showCompare);
    document.getElementById('tab-compare').setAttribute('aria-selected', showCompare);
    document.getElementById('output').classList.add('hidden');
}
document.getElementById('tab-generate').onclick = ()=> switchTab(false);
document.getElementById('tab-compare').onclick = ()=> switchTab(true);

// Character counter (modular for first textarea)
const promptTextarea = document.getElementById('prompt');
const counter = document.getElementById('counter');
promptTextarea.addEventListener('input', () => {
    const len = promptTextarea.value.length;
    counter.textContent = `${len}/1000`;
    counter.classList.toggle('limit', len > 1000);
});

// Modular output rendering
function renderGenerateOutput(data) {
    document.getElementById('output').innerHTML = `
        <h2>✨ Generated Tweet</h2>
        <p><span class="label">Tweet:</span> ${data.tweet}</p>
        <h3>🔮 Prediction</h3>
        <p>${data.prediction}</p>
        <h3>📖 Explanation</h3>
        <p>${data.explanation}</p>
    `;
    document.getElementById('output').classList.remove('hidden');
}

// Character counter (modular for second textarea)
const comparePromptTextarea = document.getElementById('comparePrompt');
const compareCounter = document.getElementById('compare-counter');
comparePromptTextarea.addEventListener('input', () => {
    const len = comparePromptTextarea.value.length;
    compareCounter.textContent = `${len}/1000`;
    compareCounter.classList.toggle('limit', len > 1000);
});


function renderCompareOutput(data) {
    document.getElementById('output').innerHTML = `
        <h2>🔬 Gemini Model A Tweet</h2>
        <p><span class="label">Tweet A:</span> ${data.model_a.tweet}</p>
        <p><span class="label">Prediction:</span> ${data.model_a.prediction}</p>
        <p><span class="label">Explanation:</span> ${data.model_a.explanation}</p>
        <h2>🔬 Gemini Model B Tweet</h2>
        <p><span class="label">Tweet B:</span> ${data.model_b.tweet}</p>
        <p><span class="label">Prediction:</span> ${data.model_b.prediction}</p>
        <p><span class="label">Explanation:</span> ${data.model_b.explanation}</p>
        <h2>🧠 Comparative Analysis</h2>
        <p><span class="label">Comparison:</span> ${data.comparison.tweet_a_vs_tweet_b}</p>
        <p><span class="label">Predicted Winner:</span> ${data.comparison.prediction}</p>
        <p><span class="label">Explanation:</span> ${data.comparison.explanation}</p>
    `;
    document.getElementById('output').classList.remove('hidden');
}

// Modular submit for Generate Tweet
document.getElementById('tweetForm').onsubmit = async function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    btn.disabled = true;
    btn.textContent = "✨ Generating...";
    try {
        const response = await fetch('/generate_tweet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: promptTextarea.value })
        });
        const data = await response.json();
        btn.disabled = false;
        btn.textContent = "✨ Generate Tweet";
        if(response.ok) renderGenerateOutput(data);
        else alert(data.error || "Error occurred.");
    } catch (err) {
        btn.disabled = false;
        btn.textContent = "✨ Generate Tweet";
        alert("Request failed!");
    }
};

// Modular submit for Compare Tweets
document.getElementById('compareForm').onsubmit = async function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitCompare');
    btn.disabled = true;
    btn.textContent = "🤝 Comparing...";
    try {
        const response = await fetch('/compare_tweets', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: comparePromptTextarea.value })  // << Send plain prompt
        }); 
        const data = await response.json();
        btn.disabled = false;
        btn.textContent = "🤝 Compare Tweets";
        if(response.ok) renderCompareOutput(data);
        else alert(data.error || "Error occurred.");
    } catch (err) {
        btn.disabled = false;
        btn.textContent = "🤝 Compare Tweets";
        alert("Request failed!");
    }
};