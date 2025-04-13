// static/js/validateRating.js

function validateRating(rating) {
  // Returns true only if rating is between 1 and 5 (inclusive)
  return rating >= 1 && rating <= 5;
}

// Attach to window for QUnit
window.validateRating = validateRating;
