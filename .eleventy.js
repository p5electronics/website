

module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("./src/css/style.css");
  eleventyConfig.addPassthroughCopy("./src/**/*.{svg,webp,png,jpeg,gif,js}"); 
	eleventyConfig.addWatchTarget("./src/css/");
	eleventyConfig.addWatchTarget("./src/**/*.{svg,webp,png,jpeg,gif,js}");
  
  eleventyConfig.addFilter("date", require("./src/filters/date.js"));

  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByTag("post").sort(function(a, b) {
      return b.date - a.date; 
    });
  });

  return {
    templateFormats: [
			"md",
			"njk",
			"html",
			"liquid",
		],

		markdownTemplateEngine: "njk",
		htmlTemplateEngine: "njk",

    dir: {
      input: "src",
      output: "public",
    }
  }
};