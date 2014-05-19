$(document).ready(function () {

    var writtenArticlesScore = 5;
    var articleLikesScore = 4;
    var writtenParagraphsScore = 3;
    var paragraphLikesScore = 2;

    var writtenArticleHTML = "";
    var articleLikesHTML = "";
    var writtenParagraphsHTML = "";
    var paragraphLikesHTML = "";

    for (var i = 0; i < writtenArticlesScore; i++) {
        writtenArticleHTML += '<i class="fa fa-star"></i>'
    }

    for (var i = 0; i < articleLikesScore; i++) {
        articleLikesHTML += '<i class="fa fa-star"></i>'
    }

    for (var i = 0; i < writtenParagraphsScore; i++) {
        writtenParagraphsHTML += '<i class="fa fa-star"></i>'
    }

    for (var i = 0; i < paragraphLikesScore; i++) {
        paragraphLikesHTML += '<i class="fa fa-star"></i>'
    }

    $(writtenArticles).html(writtenArticleHTML);
    $(articleLikes).html(articleLikesHTML);
    $(writtenParagraphs).html(writtenParagraphsHTML);
    $(paragraphLikes).html(paragraphLikesHTML);
});