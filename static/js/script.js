// Real-time password strength analyzer

const passwordInput = document.getElementById('password');
const togglePasswordBtn = document.getElementById('togglePassword');
const strengthSection = document.getElementById('strengthSection');
const strengthBar = document.getElementById('strengthBar');
const strengthValue = document.getElementById('strengthValue');
const strengthScore = document.getElementById('strengthScore');
const feedbackList = document.getElementById('feedbackList');
const issuesList = document.getElementById('issuesList');
const messageBox = document.getElementById('messageBox');
const messageText = document.getElementById('messageText');
const breachCheck = document.getElementById('breachCheck');
const breachStatus = document.getElementById('breachStatus');
const tipsList = document.getElementById('tipsList');

// Toggle password visibility
togglePasswordBtn.addEventListener('click', function() {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
});

// Real-time password checking
passwordInput.addEventListener('input', function() {
    const password = this.value;
    
    if (password.length === 0) {
        strengthSection.style.display = 'none';
        return;
    }
    
    strengthSection.style.display = 'block';
    checkPassword(password);
});

// Check password strength via API
async function checkPassword(password) {
    try {
        const response = await fetch('/api/check-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: password })
        });
        
        const data = await response.json();
        displayResults(data);
        
    } catch (error) {
        console.error('Error checking password:', error);
    }
}

// Display results
function displayResults(data) {
    // Update strength score and bar
    const score = data.score;
    strengthScore.textContent = `${score}/100`;
    strengthBar.style.width = score + '%';
    
    // Set strength level and color
    const strengthLevel = data.strength_level;
    let colorClass = '';
    
    switch(strengthLevel) {
        case 1:
            colorClass = 'strength-very-weak';
            break;
        case 2:
            colorClass = 'strength-weak';
            break;
        case 3:
            colorClass = 'strength-good';
            break;
        case 4:
            colorClass = 'strength-strong';
            break;
        case 5:
            colorClass = 'strength-very-strong';
            break;
    }
    
    strengthValue.textContent = data.strength;
    strengthValue.className = 'strength-value ' + colorClass;
    
    // Update feedback
    if (data.feedback.length > 0) {
        feedbackList.innerHTML = data.feedback
            .map(item => `<li>${item}</li>`)
            .join('');
    } else {
        feedbackList.innerHTML = '<li>No feedback yet</li>';
    }
    
    // Update issues
    if (data.issues.length > 0) {
        issuesList.innerHTML = data.issues
            .map(item => `<li>❌ ${item}</li>`)
            .join('');
    } else {
        issuesList.innerHTML = '<li>✓ No issues found</li>';
    }
    
    // Update message
    messageText.textContent = data.message;
    
    // Update breach status
    if (data.breached) {
        breachCheck.style.display = 'block';
        breachCheck.className = 'breach-check';
        breachStatus.innerHTML = '⚠️ Warning: This password has been found in a data breach! Please use a different password.';
    } else {
        breachCheck.style.display = 'block';
        breachCheck.className = 'breach-check safe';
        breachStatus.innerHTML = '✓ Safe: This password has not been found in known data breaches (as of last check).';
    }
}

// Load tips on page load
document.addEventListener('DOMContentLoaded', function() {
    loadTips();
});

// Load and display tips
async function loadTips() {
    try {
        const response = await fetch('/api/password-tips');
        const data = await response.json();
        
        tipsList.innerHTML = data.tips
            .map(tip => `<li>${tip}</li>`)
            .join('');
    } catch (error) {
        console.error('Error loading tips:', error);
    }
}

// Prevent form submission if there's a form
document.addEventListener('submit', function(e) {
    if (e.target.contains(passwordInput)) {
        e.preventDefault();
    }
});
