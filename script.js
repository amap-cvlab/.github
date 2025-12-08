document.addEventListener("DOMContentLoaded", function() {
    const repos = document.querySelectorAll("[data-github-repo]");
    
    repos.forEach(async el => {
        const repo = el.getAttribute("data-github-repo");
        try {
            const response = await fetch(`https://api.github.com/repos/${repo}`);
            if (!response.ok) throw new Error('Network response was not ok');
            
            const data = await response.json();
            const stars = data.stargazers_count;
            
            // 格式化数字: 1200 -> 1.2k
            const formatted = stars >= 1000 ? (stars / 1000).toFixed(1) + 'k' : stars;
            
            const countSpan = el.querySelector(".star-count");
            const suffixSpan = el.querySelector(".star-suffix");
            
            if (countSpan && suffixSpan) {
                countSpan.textContent = formatted;
                suffixSpan.style.display = "inline"; // 显示星星部分
            }
        } catch (error) {
            console.log("Failed to fetch stars for " + repo);
            // 失败时保持隐藏状态，不显示错误的数字
        }
    });
});
