/*
 * Source: "Calculate the estimated reading time of an article using JavaScript"
 * Link: https://dev.to/michaelburrows/calculate-the-estimated-reading-time-of-an-article-using-javascript-2k9l
 */ 

document.addEventListener('DOMContentLoaded', function() {
    function readingTime() {
      const articleElement = document.getElementById("article");
      const timeElement = document.getElementById("time");
  
      if (articleElement && timeElement) {
        const text = articleElement.innerText;
        const wpm = 225; // Words per minute
        const words = text.trim().split(/\s+/).length;
        const time = Math.ceil(words / wpm);
        timeElement.innerText = `${time} min read`; 
      } else {
        console.error('Required elements not found in the DOM.');
      }
    }
  
    readingTime();
  });
  