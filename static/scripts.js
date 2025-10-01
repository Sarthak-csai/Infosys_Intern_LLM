// Tab switching logic
function switchTab(showCompare) {
    document.getElementById('tweetForm').classList.toggle('hidden', showCompare);
    document.getElementById('compareForm').classList.toggle('hidden', !showCompare);
    document.getElementById('tab-generate').classList.toggle('active', !showCompare);
    document.getElementById('tab-generate').setAttribute('aria-selected', !showCompare);
    document.getElementById('tab-compare').classList.toggle('active', showCompare);
    document.getElementById('tab-compare').setAttribute('aria-selected', showCompare);
    document.getElementById('output').classList.add('hidden');
    // Reset buttons if tab is switched
    const genBtn = document.getElementById('submitBtn');
    const cmpBtn = document.getElementById('submitCompare');
    genBtn.disabled = false;
    genBtn.textContent = "✨ Generate Tweet";
    genBtn.classList.remove('loading');
    cmpBtn.disabled = false;
    cmpBtn.textContent = "🤝 Compare Tweets";
    cmpBtn.classList.remove('loading');
}
document.getElementById('tab-generate').onclick = () => switchTab(false);
document.getElementById('tab-compare').onclick = () => switchTab(true);

// Character counter (for first textarea)
const promptTextarea = document.getElementById('prompt');
const counter = document.getElementById('counter');
promptTextarea.addEventListener('input', () => {
    const len = promptTextarea.value.length;
    counter.textContent = `${len}/1000`;
    counter.classList.toggle('limit', len > 1000);
});

// Character counter (for second textarea)
const comparePromptTextarea = document.getElementById('comparePrompt');
const compareCounter = document.getElementById('compare-counter');
comparePromptTextarea.addEventListener('input', () => {
    const len = comparePromptTextarea.value.length;
    compareCounter.textContent = `${len}/1000`;
    compareCounter.classList.toggle('limit', len > 1000);
});

// Stylish output: Generated Tweet
function renderGenerateOutput(data) {
    document.getElementById('output').innerHTML = `
      <div class="card-out">
        <div class="card-title"><span class="card-icon">🐦</span>Generated Tweet</div>
        <div class="tweet-box"><span class="output-label">Tweet:</span> ${data.tweet}</div>
        <div class="prediction-box"><span class="output-label">Prediction:</span> ${data.prediction}</div>
        <div class="explanation-box"><span class="output-label">Explanation:</span> ${data.explanation}</div>
      </div>
    `;
    document.getElementById('output').classList.remove('hidden');
}

// Stylish output: Compare Tweets
function renderCompareOutput(data) {
    document.getElementById('output').innerHTML = `
      <div class="card-out">
        <div class="card-title"><span class="card-icon">🅰️</span>Model A Tweet</div>
        <div class="tweet-box"><span class="output-label">Tweet:</span> ${data.model_a.tweet}</div>
        <div class="prediction-box"><span class="output-label">Prediction:</span> ${data.model_a.prediction}</div>
        <div class="explanation-box"><span class="output-label">Explanation:</span> ${data.model_a.explanation}</div>
      </div>
      <div class="card-out">
        <div class="card-title"><span class="card-icon">🅱️</span>Model B Tweet</div>
        <div class="tweet-box"><span class="output-label">Tweet:</span> ${data.model_b.tweet}</div>
        <div class="prediction-box"><span class="output-label">Prediction:</span> ${data.model_b.prediction}</div>
        <div class="explanation-box"><span class="output-label">Explanation:</span> ${data.model_b.explanation}</div>
      </div>
      <div class="analysis-card">
        <div class="card-title"><span class="card-icon">🔍</span>Comparative Analysis</div>
        <div style="margin-bottom:0.7em;"><span class="output-label">Comparison:</span> ${data.comparison.tweet_a_vs_tweet_b}</div>
        <div style="margin-bottom:0.6em;">
          <span class="output-label">Predicted Winner:</span> 
          <span class="winner-tag">${data.comparison.prediction}</span>
        </div>
        <div class="explanation-box"><span class="output-label">Explanation:</span> ${data.comparison.explanation}</div>
      </div>
    `;
    document.getElementById('output').classList.remove('hidden');
}

// Form submit: Generate Tweet
document.getElementById('tweetForm').onsubmit = async function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    if (btn.disabled) return;
    btn.disabled = true;
    btn.classList.add('loading');
    btn.textContent = "⏳ Generating...";
    try {
        const response = await fetch('/generate_tweet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: promptTextarea.value })
        });
        const data = await response.json();
        btn.disabled = false;
        btn.classList.remove('loading');
        btn.textContent = "✨ Generate Tweet";
        if (response.ok) {
            renderGenerateOutput(data);
        } else {
            alert(data.error || "Error occurred.");
        }
    } catch (err) {
        btn.disabled = false;
        btn.classList.remove('loading');
        btn.textContent = "✨ Generate Tweet";
        alert("Request failed!");
    }
};

// Form submit: Compare Tweets
document.getElementById('compareForm').onsubmit = async function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitCompare');
    if (btn.disabled) return;
    btn.disabled = true;
    btn.classList.add('loading');
    btn.textContent = "⏳ Comparing...";
    try {
        const response = await fetch('/compare_tweets', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: comparePromptTextarea.value })
        });
        const data = await response.json();
        btn.disabled = false;
        btn.classList.remove('loading');
        btn.textContent = "🤝 Compare Tweets";
        if (response.ok) {
            renderCompareOutput(data);
        } else {
            alert(data.error || "Error occurred.");
        }
    } catch (err) {
        btn.disabled = false;
        btn.classList.remove('loading');
        btn.textContent = "🤝 Compare Tweets";
        alert("Request failed!");
    }
};
